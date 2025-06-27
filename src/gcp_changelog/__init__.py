from typing import Self
from datetime import date
from dateutil import parser
from typing import Generator
from markdownify import markdownify as md
from dataclasses import dataclass
import asyncio

import httpx


@dataclass
class ProductChangelog:
    content: list[str]
    kind: str | None = None

    @property
    def as_markdown(self) -> str:
        return str(md("\n".join(str(c) for c in self.content)))

    def __str__(self) -> str:
        texts = [
            "==============",
            f"Product: {self.kind}",
            f"Content: {self.as_markdown}",
            "==============",
        ]
        return "\n".join(texts)

    __repr__ = __str__


@dataclass
class Product:
    name: str
    entries: list[ProductChangelog]
    date: date = None

    @property
    def slug(self) -> str:
        return self.name.lower().replace(" ", "-").replace("/", "")


@dataclass
class ProductIndex:
    name: str
    changelog: list[Product]


@dataclass
class Index:
    products: dict[str, ProductIndex]

    @classmethod
    def new(cls) -> Self:
        return cls(products={})

    def add(self, product: Product) -> None:
        slug = product.slug

        if slug not in self.products:
            i = ProductIndex(name=product.name, changelog=[])
            self.products[slug] = i
        else:
            i = self.products[slug]

        i.changelog.append(product)



    def save(self) -> None:
        for slug, product in self.products.items():
            filename = f"data/{slug}.md"
            with open(filename, "w") as fp:
                fp.write(f"# {product.name}\n")
                fp.write("\n")

                for entry in reversed(sorted(product.changelog, key=lambda p: p.date)):
                    fp.write(f"## {entry.date}\n")
                    fp.write("\n")
                    for changelog in entry.entries:
                        fp.write(f"### {changelog.kind}\n")
                        fp.write("\n")
                        fp.write(changelog.as_markdown)






async def async_main() -> None:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://cloud.google.com/feeds/gcp-release-notes.xml"
        )

        index = parse_atom_feed(response.text)
        index.save()


def parse_atom_feed(feed: str) -> Index:
    from xml.etree import ElementTree

    index = Index.new()

    root = ElementTree.fromstring(feed)
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        content = entry.find("{http://www.w3.org/2005/Atom}content")
        assert content is not None
        assert content.text is not None

        date_element = entry.find("{http://www.w3.org/2005/Atom}updated")
        assert date_element is not None
        date = parser.parse(date_element.text)

        assert content.attrib["type"] == "html"

        for product in parse_content(content.text):
            product.date = date
            index.add(product)


    return index





def parse_content(content: str) -> Generator[Product]:
    from bs4 import BeautifulSoup

    page = BeautifulSoup(content, "html.parser")

    products = page.findAll("h2")

    for product in products:
        product_name = product.text.strip()
        print(product_name)

        p = Product(name=product_name, entries=[])

        entry: ProductChangelog | None = None

        for sibling in product.next_siblings:
            if sibling.name == "h3":
                if entry is not None:
                    p.entries.append(entry)

                kind = sibling.text.strip()
                entry = ProductChangelog(kind=kind, content=[])

            elif sibling.name == "h2":
                break

            else:
                if entry is None:
                    continue
                entry.content.append(sibling)

        if entry is not None:
            p.entries.append(entry)

        yield p


def main() -> None:
    asyncio.run(async_main())
