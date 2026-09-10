# rich renderables

`rich_to_ansi` bridges [rich](https://rich.readthedocs.io) with `prompt_toolkit`. It
renders any rich renderable — or a string containing rich markup — into a
`prompt_toolkit.formatted_text.ANSI` object, which can be used anywhere formatted text
is accepted: choice names, `PreviewPrompt` previews, and so on.

## Install

The integration is an optional extra:

```sh
pip install "InquirerPrompt[rich]"
```

## Usage

```python
from prompt_toolkit.formatted_text import HTML
from rich.text import Text

from InquirerPrompt import inquirer
from InquirerPrompt.base.control import Choice
from InquirerPrompt.utils import rich_to_ansi


def main():
    result = inquirer.select(
        message="Select a status:",
        choices=[
            Choice("ok", name=rich_to_ansi("[bold green]✓ OK[/bold green]")),
            Choice("warn", name=rich_to_ansi("[bold yellow]⚠ Warning[/bold yellow]")),
            Choice("err", name=rich_to_ansi("[bold red]✗ Error[/bold red]")),
        ],
        border=True,
    ).execute()
    print(result)


if __name__ == "__main__":
    main()
```

Rich renderables such as `Text`, `Table` or `Panel` are supported as well:

```python
Choice("zsh", name=rich_to_ansi(Text("zsh", style="bright_cyan")))
```

```{warning}
List prompts render choice names on a single line. Keep renderables single-line
(or pass `width`) when using them as choice names.
```

## Notes

- Plain string choice names continue to work unchanged; use `rich_to_ansi`
  explicitly to opt in.
- `rich_to_ansi` raises `InvalidArgument` with an install hint when `rich` is not
  available.
- The rendered ANSI is accepted by `expand_formatted_text`, so per-choice colors
  and the pointer/hover style are merged the same way as `HTML`/`ANSI` choice
  names (see {ref}`pages/prompts/list:Choices`).

## See Also

- Demo: `examples/rich_choices.py`
