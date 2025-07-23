import datetime
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Iterator
from typing import Self

from pydantic import BaseModel

STANDARD_KINDS = {
    "Announcement",
    "Breaking",
    "Changed",
    "Deprecated",
    "Feature",
    "Fixed",
    "Issue",
    "Libraries",
    "Security",
}


@dataclass
class Config:
    content_folder: Path

    def ensure(self) -> None:
        self.content_folder.mkdir(parents=True, exist_ok=True)

    @property
    def site_index(self) -> Path:
        return self.content_folder / "index.md"

    def folder_for(self, slug: str) -> Path:
        return self.content_folder / slug

    @property
    def json_files(self) -> Iterator[Path]:
        return self.content_folder.glob("*/*.json")


class Summary(BaseModel):
    title: str
    summary: str


class ChangelogEntry(BaseModel):
    kind: str
    content: str

    summary: Summary | None = None

    def __hash__(self) -> int:
        return hash(f"{self.kind}{self.content}")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False

        return (
            self.kind.strip() == other.kind.strip()
            and self.content.strip() == other.content.strip()
        )


class ProductChangelog(BaseModel):
    name: str
    entries: dict[datetime.date, list[ChangelogEntry]]

    @property
    def slug(self) -> str:
        return re.sub(r"[^a-z0-9\-_]", "-", self.name.lower())

    @classmethod
    def load(cls, filename: Path) -> Self:
        return cls.model_validate_json(filename.read_text())

    def dump(self, filename: Path) -> None:
        with open(str(filename), "w") as fp:
            fp.write(self.model_dump_json(indent=2))

    def render(self, filename: Path) -> None:
        with open(filename, "w") as fp:
            fp.write(f"# {self.name}\n")
            fp.write("\n")

            for date in reversed(sorted(self.entries)):
                changelog = self.entries[date]
                fp.write(f"## {date.strftime('%Y-%m-%d')}\n")
                fp.write("\n")

                for entry in changelog:
                    fp.write(f"### {entry.kind}\n")
                    fp.write("\n")
                    fp.write(entry.content)
                    fp.write("\n")
                    fp.write("\n")

                fp.write("---\n")

    def absorb(self, other: Self) -> None:
        for date, other_entries in other.entries.items():
            if date in self.entries:
                self.entries[date] = list(self._merge_entries(date, other_entries))
            else:
                self.entries[date] = other_entries

    def _merge_entries(
        self, date: datetime.date, olders: list[ChangelogEntry]
    ) -> Iterator[ChangelogEntry]:
        # We prioritize what we parsed now, instead of what we parsed before.
        #
        # What we parsed before: if the "entries" match, we keep the old one,
        # which may contain an already built summary.
        #
        # Otherwise, we assume the new one "wins" and we discard the old one.

        _olders = set(olders)

        entries = self.entries[date]

        for entry in entries:
            if entry.content.strip() == "" and entry.kind in STANDARD_KINDS:
                # No description, let's skip it
                continue

            for older in _olders:
                if older == entry:
                    # _olders.remove(older)
                    entry.summary = older.summary
                    yield entry
                    break
            else:
                # The entry we parsed is new (or a rewrite of an old one)
                # We keep it as it is in this case.
                yield entry


class Index(BaseModel):
    products: dict[str, ProductChangelog] = {}

    @classmethod
    def load(cls, config: Config) -> Self:
        products: dict[str, ProductChangelog] = {}

        for json_file in config.json_files:
            product = ProductChangelog.load(json_file)
            products[product.name] = product

        return cls(products=products)

    def total_size(self) -> int:
        return sum(
            1
            for product in self.products.values()
            for entries in product.entries.values()
            for entry in entries
        )

    def dump(self, config: Config) -> None:
        for product in self.products.values():
            slug = product.slug

            filename = config.folder_for(slug) / "index.json"
            filename.parent.mkdir(parents=True, exist_ok=True)
            product.dump(filename)

    def render(self, config: Config) -> None:
        index: dict[str, Path] = {}

        for key, product in self.products.items():
            slug = product.slug
            print(f"Rendering product: {key} ({slug})")

            filename = config.folder_for(slug) / "index.md"
            product.render(filename)
            index[product.name] = filename

            from .atom import build_feed

            feed = build_feed(product)

            filename = config.folder_for(slug) / "feed.atom"
            with open(str(filename), "w") as fp:
                feed.write(fp, encoding="unicode", xml_declaration=True)

        with open(config.site_index, "w") as fp:
            fp.write("# Google Cloud Platform Release Notes (by services)\n")
            fp.write("\n")

            for name, path in sorted(index.items()):
                filename = path.relative_to(config.content_folder)
                fp.write(f"- [{name}]({filename})\n")

    def absorb(self, other: Self) -> None:
        for name, other_product in other.products.items():
            if (self_product := self.products.get(name)) is not None:
                self_product.absorb(other_product)
            else:
                self.products[name] = other_product
