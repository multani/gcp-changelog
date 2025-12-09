from datetime import date
from typing import Generator
from typing import cast
from xml.etree import ElementTree

import bs4
import dateutil.parser
import httpx
from markdownify import markdownify  # type: ignore

from . import models
from .exceptions import InvalidFeed


def fetch_feed(url: str) -> models.Index:
    with httpx.Client() as client:
        response = client.get(url, follow_redirects=True)

    index = parse_atom_feed(response.text)
    return index


def parse_atom_feed(feed: str) -> models.Index:
    index = models.Index()

    ns = {
        "atom": "http://www.w3.org/2005/Atom",
    }

    try:
        root = ElementTree.fromstring(feed)
    except ElementTree.ParseError as e:
        raise InvalidFeed("Failed to parse Atom feed", feed=feed) from e

    for atom_entry in root.findall("atom:entry", ns):
        content = atom_entry.find("atom:content", ns)
        assert content is not None
        assert content.text is not None

        date_element = atom_entry.find("atom:updated", ns)
        assert date_element is not None
        assert date_element.text is not None
        date = dateutil.parser.parse(date_element.text)

        assert content.attrib["type"] == "html"

        for product in parse_single_date(content.text, date):
            if (old_product := index.products.get(product.name)) is not None:
                old_product.absorb(product)
            else:
                index.products[product.name] = product

    return index


def parse_single_date(content: str, date: date) -> Generator[models.ProductChangelog]:
    page = bs4.BeautifulSoup(content, "lxml")

    products = page.find_all("h2")

    for product in products:
        entries: list[models.ChangelogEntry] = []

        product_name = product.text.strip()

        entries = [entry for entry in parse_product_updates(product)]

        product_changelog = models.ProductChangelog(
            name=product_name,
            entries={date: entries},
        )

        yield product_changelog


def parse_product_updates(product: bs4.Tag) -> Generator[models.ChangelogEntry]:
    kind: str | None = None
    content: list[bs4.PageElement] = []

    # Loop until the next h2
    # The next h2 is the next product
    for sibling in product.next_siblings:
        sibling = cast(bs4.Tag, sibling)

        if sibling.name == "h3":
            # This is a new announcement/feature/changes for this product.
            if kind is not None:
                entry = models.ChangelogEntry(kind=kind, content=as_markdown(content))
                yield entry

            kind = sibling.text.strip()
            content = []

        elif sibling.name == "h2":
            break

        else:
            if kind is None:
                continue
            content.append(sibling)

    if kind is not None:
        entry = models.ChangelogEntry(kind=kind, content=as_markdown(content))
        yield entry


def as_markdown(content: list[bs4.PageElement]) -> str:
    return str(markdownify("\n".join(str(c) for c in content)))
