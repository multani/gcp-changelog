import datetime
import re
from pathlib import Path
from typing import Self

from pydantic import BaseModel


class ChangelogEntry(BaseModel):
    kind: str
    content: str


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
                continue
            self.entries[date] = other_entries


class Index(BaseModel):
    products: dict[str, ProductChangelog] = {}

    @classmethod
    def load(cls, folder: Path) -> Self:
        products: dict[str, ProductChangelog] = {}

        for json_file in folder.glob("*.json"):
            product = ProductChangelog.load(json_file)
            products[product.name] = product

        return cls(products=products)

    def dump(self, folder: Path) -> None:
        for product in self.products.values():
            slug = product.slug

            filename = folder / f"{slug}.json"
            product.dump(filename)

    def render(self, folder: Path) -> None:
        index: dict[str, Path] = {}

        for product in self.products.values():
            slug = product.slug

            filename = folder / "services" / f"{slug}.md"
            product.render(filename)
            index[product.name] = filename

        with open(folder / "index.md", "w") as fp:
            fp.write("# Google Cloud Platform Release Notes (by services)\n")
            fp.write("\n")

            for name, path in sorted(index.items()):
                filename = path.relative_to(folder)
                fp.write(f"- [{name}]({filename})\n")

    def absorb(self, other: Self) -> None:
        for name, other_product in other.products.items():
            if (self_product := self.products.get(name)) is not None:
                self_product.absorb(other_product)
            else:
                self.products[name] = other_product
