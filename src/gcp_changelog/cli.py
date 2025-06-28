from dataclasses import dataclass
from pathlib import Path

import click

from . import models
from .parser import fetch_feed


def main() -> None:
    cli()


@dataclass
class Config:
    data_folder: Path


pass_config = click.make_pass_decorator(Config)


@click.group()
@click.option(
    "--data-folder",
    default="data/json",
    help="Folder to save the parsed data",
    type=click.Path(dir_okay=True, path_type=Path),
)
@click.pass_context
def cli(ctx: click.Context, data_folder: Path) -> None:
    config = ctx.obj = Config(data_folder=data_folder)
    config.data_folder.mkdir(parents=True, exist_ok=True)


@cli.command()
@click.option(
    "--url",
    default="https://cloud.google.com/feeds/gcp-release-notes.xml",
    help="URL of the GCP release notes feed.",
)
@pass_config
def fetch(config: Config, url: str) -> None:
    print("Loading existing data...")
    original_index = models.Index.load(config.data_folder)

    print(f"Fetching feed from {url=}...")
    url = "https://cloud.google.com/feeds/gcp-release-notes.xml"
    index = fetch_feed(url)

    print("Merging fetched data with previous data...")
    index.absorb(original_index)

    print(f"Saving data to: {config.data_folder}")
    index.dump(config.data_folder)

    print("Done!")


@cli.command()
@click.option(
    "--render-folder",
    default="data/markdown",
    help="Folder to renderd the content to",
    type=click.Path(dir_okay=True, path_type=Path),
)
@pass_config
def render(config: Config, render_folder: Path) -> None:
    print(f"Loading existing data from: {config.data_folder}")
    index = models.Index.load(config.data_folder)

    print(f"Rendering data to: {render_folder}")
    render_folder.mkdir(parents=True, exist_ok=True)
    index.render(render_folder)

    print("Done!")
