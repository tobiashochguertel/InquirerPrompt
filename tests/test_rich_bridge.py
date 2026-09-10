"""Tests for the rich -> prompt_toolkit bridge utility."""

import sys
import unittest
from unittest.mock import patch

from prompt_toolkit.formatted_text import ANSI, to_formatted_text
from rich.table import Table
from rich.text import Text

from InquirerPrompt.exceptions import InvalidArgument
from InquirerPrompt.utils import expand_formatted_text, rich_to_ansi


def _plain_text(result) -> str:
    return "".join(fragment[1] for fragment in to_formatted_text(result))


def _styles(result) -> str:
    return " ".join(fragment[0] for fragment in to_formatted_text(result))


class TestRichToAnsi(unittest.TestCase):
    """Test :func:`InquirerPrompt.utils.rich_to_ansi`."""

    def test_markup_string(self) -> None:
        result = rich_to_ansi("[bold green]✓ OK[/bold green]")
        self.assertIsInstance(result, ANSI)
        self.assertEqual(_plain_text(result), "✓ OK")
        self.assertIn("ansigreen", _styles(result))

    def test_rich_renderable(self) -> None:
        result = rich_to_ansi(Text("hello", style="red"))
        self.assertEqual(_plain_text(result), "hello")
        self.assertIn("ansired", _styles(result))

    def test_table_renderable(self) -> None:
        table = Table("Name", "Value")
        table.add_row("alpha", "1")
        text = _plain_text(rich_to_ansi(table))
        self.assertIn("Name", text)
        self.assertIn("alpha", text)

    def test_width_wraps(self) -> None:
        result = rich_to_ansi("word " * 20, width=20)
        self.assertGreater(len(_plain_text(result).splitlines()), 1)

    def test_color_system_256(self) -> None:
        result = rich_to_ansi("[color(200)]pink[/color(200)]", color_system="256")
        self.assertEqual(_plain_text(result), "pink")

    def test_bridge_result_works_as_choice_name(self) -> None:
        fragments = expand_formatted_text(
            "class:pointer", rich_to_ansi("[green]✓ Info[/green]")
        )
        self.assertEqual("".join(fragment[1] for fragment in fragments), "✓ Info")
        self.assertTrue(all("class:pointer" in fragment[0] for fragment in fragments))
        self.assertIn("ansigreen", " ".join(fragment[0] for fragment in fragments))

    def test_missing_rich_dependency(self) -> None:
        with patch.dict(sys.modules, {"rich.console": None}):
            with self.assertRaises(InvalidArgument) as context:
                rich_to_ansi("hello")
        self.assertIn("InquirerPrompt[rich]", str(context.exception))


if __name__ == "__main__":
    unittest.main()
