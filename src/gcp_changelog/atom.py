import datetime
from typing import Iterator

import markdown
from lxml import etree

from .models import ProductChangelog


def date_to_datetime(d: datetime.date) -> str:
    dt = datetime.datetime.fromisoformat(d.isoformat())
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt.isoformat()


def build_feed(changelog: ProductChangelog) -> etree._ElementTree:
    attributes = {
        "xmlns": "http://www.w3.org/2005/Atom",
    }
    feed = etree.Element("feed", attrib=attributes)

    feed.extend(build_metadata(changelog))
    feed.extend(build_entries(changelog))

    etree.indent(feed, space="  ", level=0)
    return etree.ElementTree(feed)


def build_metadata(changelog: ProductChangelog) -> Iterator[etree._Element]:
    last_date = max(changelog.entries.keys())

    fields = {
        "title": f"Google Cloud: {changelog.name}",
        "subtitle": f"Changelog for Google Cloud product: {changelog.name}",
        "updated": date_to_datetime(last_date),
        "id": f"urn:github:multani:gcp-changelog:{changelog.slug}",
    }

    for key, value in fields.items():
        element = etree.Element(key)
        element.text = value
        yield element

    slug = changelog.slug
    self_link = f"https://raw.githubusercontent.com/multani/gcp-changelog/refs/heads/main/content/{slug}/"

    element = etree.Element("link")
    element.set("rel", "self")
    element.set("href", self_link)
    yield element


def build_entries(product_changelog: ProductChangelog) -> Iterator[etree._Element]:
    for date, changelog_entries in product_changelog.entries.items():
        for i, changelog in enumerate(changelog_entries):
            elements = []

            author = etree.Element("author")
            author_name = etree.Element("name")
            author_name.text = "Google Cloud"
            author.append(author_name)
            elements.append(author)

            id = f"{date.isoformat()}:{changelog.kind}:{i}".lower()

            entry_id = etree.Element("id")
            entry_id.text = (
                f"urn:github:multani:gcp-changelog:{product_changelog.slug}:{id}"
            )
            elements.append(entry_id)

            published = etree.Element("published")
            published.text = date_to_datetime(date)
            elements.append(published)

            updated = etree.Element("updated")
            updated.text = published.text
            elements.append(updated)

            content = etree.Element("content")
            content.set("type", "html")
            content.text = etree.CDATA(markdown.markdown(changelog.content))
            elements.append(content)

            if changelog.summary is not None:
                summary = etree.Element("summary")
                summary.text = changelog.summary.summary
                elements.append(summary)

                title = etree.Element("title")
                title.text = f"{changelog.kind}: {changelog.summary.title}"
                elements.append(title)

            x = etree.Element("entry")
            x.extend(elements)
            yield x
