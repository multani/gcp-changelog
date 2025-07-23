import datetime
from typing import Iterator
from xml.etree import ElementTree as ET

from .models import ProductChangelog


def date_to_datetime(d: datetime.date) -> str:
    dt =datetime.datetime.fromisoformat(d.isoformat())
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt.isoformat()


def build_feed(changelog: ProductChangelog) -> ET.ElementTree:
    attributes = {
        "xmlns": "http://www.w3.org/2005/Atom",
        "xml:lang": "en",
    }
    feed = ET.Element("feed", attrib=attributes)

    feed.extend(build_metadata(changelog))
    feed.extend(build_entries(changelog))

    ET.indent(feed, space="  ", level=0)
    return ET.ElementTree(feed)


def build_metadata(changelog: ProductChangelog) -> Iterator[ET.Element]:
    last_date = max(changelog.entries.keys())

    fields = {
        "title": f"Google Cloud: {changelog.name}",
        "subtitle": f"Changelog for Google Cloud product: {changelog.name}",
        "updated": date_to_datetime(last_date),
        "id": f"urn:github:multani:gcp-changelog:{changelog.slug}",
    }

    for key, value in fields.items():
        element = ET.Element(key)
        element.text = value
        yield element

    slug = changelog.slug
    self_link = f"https://raw.githubusercontent.com/multani/gcp-changelog/refs/heads/main/content/{slug}/"

    element = ET.Element("link")
    element.set("rel", "self")
    element.set("href", self_link)
    yield element


def build_entries(product_changelog: ProductChangelog) -> Iterator[ET.Element]:
    for date, changelog_entries in product_changelog.entries.items():
        for i, changelog in enumerate(changelog_entries):
            elements = []

            title = ET.Element("title")
            title.text = changelog.kind
            elements.append(title)

            author = ET.Element("author")
            author_name = ET.Element("name")
            author_name.text = "Google Cloud"
            author.append(author_name)
            elements.append(author)

            id = f"{date.isoformat()}:{changelog.kind}:{i}".lower()

            entry_id = ET.Element("id")
            entry_id.text = f"urn:github:multani:gcp-changelog:{product_changelog.slug}:{id}"
            elements.append(entry_id)

            published = ET.Element("published")
            published.text = date_to_datetime(date)
            elements.append(published)

            updated = ET.Element("updated")
            updated.text = published.text
            elements.append(updated)

            # summary = ET.Element("summary")
            content = ET.Element("content")
            content.set("type", "text/markdown")
            content.text = changelog.content
            elements.append(content)

            x = ET.Element("entry")
            x.extend(elements)
            yield x
