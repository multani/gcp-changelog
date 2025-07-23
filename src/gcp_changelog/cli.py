from pathlib import Path

import click

from . import models
from .parser import fetch_feed

pass_config = click.make_pass_decorator(models.Config)


def main() -> None:
    cli()


@click.group()
@click.option(
    "--contents-folder",
    default="content",
    help="Folder to save the parsed data",
    type=click.Path(dir_okay=True, path_type=Path),
)
@click.pass_context
def cli(ctx: click.Context, contents_folder: Path) -> None:
    config = ctx.obj = models.Config(content_folder=contents_folder)
    config.ensure()


@cli.command()
@click.option(
    "--url",
    default="https://cloud.google.com/feeds/gcp-release-notes.xml",
    help="URL of the GCP release notes feed.",
)
@pass_config
def fetch(config: models.Config, url: str) -> None:
    print("Loading existing data...")
    original_index = models.Index.load(config)

    print(f"Fetching feed from {url=}...")
    url = "https://cloud.google.com/feeds/gcp-release-notes.xml"
    index = fetch_feed(url)

    print("Merging fetched data with previous data...")
    index.absorb(original_index)

    print(f"Saving data to: {config.content_folder}")
    index.dump(config)

    print("Done!")


@cli.command()
@pass_config
def render(config: models.Config) -> None:
    print(f"Loading existing data from: {config.content_folder}")
    index = models.Index.load(config)

    print("Rendering data")
    index.render(config)

    print("Done!")

