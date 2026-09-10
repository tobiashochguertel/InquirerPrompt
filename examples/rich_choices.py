#!/usr/bin/env python3
"""Manual test script for rich renderables as choice names.

Requires the optional rich dependency:

    pip install InquirerPrompt[rich]

Run in a terminal:

    python examples/rich_choices.py
"""

from rich.text import Text

from InquirerPrompt import inquirer
from InquirerPrompt.base.control import Choice
from InquirerPrompt.separator import Separator
from InquirerPrompt.utils import rich_to_ansi


def test_markup():
    """ListPrompt with rich markup strings as choice names."""
    print("\n=== select (rich markup) ===")
    result = inquirer.select(
        message="Select a status:",
        choices=[
            Choice("ok", name=rich_to_ansi("[bold green]✓ OK[/bold green]")),
            Choice("warn", name=rich_to_ansi("[bold yellow]⚠ Warning[/bold yellow]")),
            Choice("err", name=rich_to_ansi("[bold red]✗ Error[/bold red]")),
            Separator(),
            Choice(
                "info",
                name=rich_to_ansi("[dim]ℹ More info[/dim]"),
            ),
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


def test_rich_text():
    """ListPrompt with rich Text renderables as choice names."""
    print("\n=== select (rich Text) ===")
    result = inquirer.select(
        message="Select a shell:",
        choices=[
            Choice("zsh", name=rich_to_ansi(Text("zsh", style="bright_cyan"))),
            Choice("bash", name=rich_to_ansi(Text("bash", style="green"))),
            Choice("fish", name=rich_to_ansi(Text("fish", style="bright_magenta"))),
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


def test_checkbox():
    """CheckboxPrompt with rich markup choice names."""
    print("\n=== checkbox (rich markup) ===")
    result = inquirer.checkbox(
        message="Select features:",
        choices=[
            Choice("search", name=rich_to_ansi("[green]✓ Search[/green]")),
            Choice("ai", name=rich_to_ansi("[green]✓ AI[/green]")),
            Choice("telemetry", name=rich_to_ansi("[red]✗ Telemetry[/red]")),
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


if __name__ == "__main__":
    print("InquirerPrompt Rich Choices Demo")
    print("=" * 40)
    test_markup()
    test_rich_text()
    test_checkbox()
    print("\n✓ All demos complete!")
