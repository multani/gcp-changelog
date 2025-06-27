import asyncio
from pathlib import Path

import httpx

from . import models, parser


async def async_main() -> None:
    async with httpx.AsyncClient() as client:
        url = "https://cloud.google.com/feeds/gcp-release-notes.xml"
        response = await client.get(url)

        index = parser.parse_atom_feed(response.text)
        save(index)


def save(index: models.Index) -> None:
    folder = Path("data")
    folder.mkdir(parents=True, exist_ok=True)

    original_index = models.Index.load(folder)
    index.absorb(original_index)

    index.dump(folder)
    index.render(folder)


def main() -> None:
    asyncio.run(async_main())
