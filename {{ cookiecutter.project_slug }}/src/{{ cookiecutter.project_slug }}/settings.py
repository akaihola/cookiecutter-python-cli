from dataclasses import dataclass, field


def mkhelp(help_text: str) -> dict[str, dict[str, str]]:
    return {"typed-settings": {"help": help_text}}


@dataclass
class Settings:
    optional_integer: int | None = field(
        default=None,
        metadata=mkhelp("An example optional integer setting"),
    )
    optional_string: str | None = field(
        default=None,
        metadata=mkhelp("An optional string setting"),
    )
    boolean: bool = field(
        default=False,
        metadata=mkhelp("An example boolean setting"),
    )
