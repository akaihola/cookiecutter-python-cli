from dataclasses import dataclass, field


def mkhelp(help_text: str) -> dict[str, dict[str, str]]:
    return {"typed-settings": {"help": help_text}}


@dataclass
class Settings:
    show_config: bool = field(
        default=False,
        metadata=mkhelp("Show the effective configuration and exit"),
    )
    optional_integer: int | None = field(
        default=None,
        metadata=mkhelp("An example optional integer setting"),
    )
    optional_string: str | None = field(
        default=None,
        metadata=mkhelp("An optional string setting"),
    )
