from datetime import date
from typing import Generator, cast
from xml.etree import ElementTree

import bs4
import dateutil.parser
from markdownify import markdownify  # type: ignore

from . import models


def as_markdown(content: list[bs4.PageElement]) -> str:
    return str(markdownify("\n".join(str(c) for c in content)))


def parse_atom_feed(feed: str) -> models.Index:
    index = models.Index()

    root = ElementTree.fromstring(feed)
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        content = entry.find("{http://www.w3.org/2005/Atom}content")
        assert content is not None
        assert content.text is not None

        date_element = entry.find("{http://www.w3.org/2005/Atom}updated")
        assert date_element is not None
        assert date_element.text is not None
        date = dateutil.parser.parse(date_element.text)

        assert content.attrib["type"] == "html"

        for pc in parse_single_date(content.text, date):
            if (old_pc := index.products.get(pc.name)) is not None:
                old_pc.absorb(pc)
            else:
                index.products[pc.name] = pc

    return index


def parse_single_date(content: str, date: date) -> Generator[models.ProductChangelog]:
    page = bs4.BeautifulSoup(content, "html.parser")

    products = page.findAll("h2")

    for product in products:
        cel: list[models.ChangelogEntry] = []

        product_name = product.text.strip()

        for ce in parse_product_updates(product):
            cel.append(ce)

        pc = models.ProductChangelog(
            name=product_name,
            entries={date: cel},
        )

        yield pc


def parse_product_updates(product: bs4.Tag) -> Generator[models.ChangelogEntry]:
    kind: str | None = None
    content: list[bs4.PageElement] = []

    for sibling in product.next_siblings:
        sibling = cast(bs4.Tag, sibling)

        if sibling.name == "h3":
            if kind is not None:
                ce = models.ChangelogEntry(kind=kind, content=as_markdown(content))
                yield ce

            kind = sibling.text.strip()
            content = []

        elif sibling.name == "h2":
            break

        else:
            if kind is None:
                continue
            content.append(sibling)

    if kind is not None:
        ce = models.ChangelogEntry(kind=kind, content=as_markdown(content))
        yield ce
