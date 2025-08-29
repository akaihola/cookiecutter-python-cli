import dataclasses
from platformdirs import user_config_path

import click
import typed_settings as ts

from {{ cookiecutter.project_package }}.settings import Settings


@click.command()
@ts.click_options(
    Settings,
    ts.default_loaders("{{ cookiecutter.project_slug }}", [user_config_path("{{ cookiecutter.project_slug }}.toml")]),
)
def main(settings: Settings) -> None:
    """A command line tool to ..."""
    # Show the effective configuration and exit if --show-config is used
    if settings.show_config:
        click.echo(f"Effective configuration: {dataclasses.asdict(settings)}")
        return


if __name__ == "__main__":
    main()
