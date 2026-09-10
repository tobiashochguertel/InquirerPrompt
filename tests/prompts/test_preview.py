"""Tests for the preview prompt and its content conversion."""

import unittest
from unittest.mock import patch

from prompt_toolkit.formatted_text import HTML
from rich.text import Text

from InquirerPrompt import inquirer
from InquirerPrompt.exceptions import InvalidArgument
from InquirerPrompt.prompts.preview import PreviewPrompt, format_preview_text


class TestFormatPreviewText(unittest.TestCase):
    """Test :func:`InquirerPrompt.prompts.preview.format_preview_text`."""

    def test_plain_string(self):
        self.assertEqual(format_preview_text("hello"), [("", "hello")])

    def test_html(self):
        self.assertEqual(
            format_preview_text(HTML("<ansigreen>ok</ansigreen>")),
            [("class:ansigreen", "ok")],
        )

    def test_rich_renderable(self):
        fragments = format_preview_text(Text("rich", style="red"))
        self.assertEqual("".join(f[1] for f in fragments), "rich")
        self.assertIn("ansired", " ".join(f[0] for f in fragments))


class TestPreviewPrompt(unittest.TestCase):
    """Test :class:`InquirerPrompt.prompts.preview.PreviewPrompt`."""

    def test_preview_follows_highlighted_choice(self):
        prompt = PreviewPrompt(
            message="Pick:",
            choices=["a", "b"],
            preview=lambda value: "Preview: %s" % value,
        )
        self.assertEqual(prompt._get_preview_text(), [("", "Preview: a")])
        prompt.content_control.selected_choice_index = 1
        self.assertEqual(prompt._get_preview_text(), [("", "Preview: b")])

    def test_preview_default_selection(self):
        prompt = PreviewPrompt(
            message="Pick:", choices=["a", "b"], preview=str.upper, default="b"
        )
        self.assertEqual(prompt._get_preview_text(), [("", "B")])

    def test_preview_formatted_text(self):
        prompt = PreviewPrompt(
            message="Pick:",
            choices=["a"],
            preview=lambda value: HTML("<ansigreen>ok</ansigreen>"),
        )
        self.assertEqual(prompt._get_preview_text(), [("class:ansigreen", "ok")])

    def test_preview_rich_renderable(self):
        prompt = PreviewPrompt(
            message="Pick:",
            choices=["a"],
            preview=lambda value: Text("rich", style="red"),
        )
        self.assertEqual("".join(f[1] for f in prompt._get_preview_text()), "rich")

    def test_preview_error_is_displayed(self):
        def broken(value):
            raise ValueError("boom")

        prompt = PreviewPrompt(message="Pick:", choices=["a"], preview=broken)
        self.assertIn(
            "Preview error: boom", "".join(f[1] for f in prompt._get_preview_text())
        )

    def test_preview_must_be_callable(self):
        self.assertRaises(InvalidArgument, PreviewPrompt, "Pick:", ["a"], None)

    def test_preview_separator_container(self):
        prompt = PreviewPrompt(
            message="Pick:", choices=["a"], preview=lambda value: value
        )
        self.assertEqual(len(prompt._extra_content_containers()), 2)

        prompt = PreviewPrompt(
            message="Pick:",
            choices=["a"],
            preview=lambda value: value,
            preview_separator=False,
        )
        self.assertEqual(len(prompt._extra_content_containers()), 1)

    def test_preview_height(self):
        prompt = PreviewPrompt(
            message="Pick:",
            choices=["a"],
            preview=lambda value: value,
            preview_height=4,
        )
        self.assertEqual(prompt._dimmension_preview_height, 4)

    def test_inquirer_preview_entry_point(self):
        self.assertIs(inquirer.preview, PreviewPrompt)

    @patch("InquirerPrompt.base.complex.Application.run")
    def test_prompt_execute(self, mocked_run):
        mocked_run.return_value = "hello"
        result = PreviewPrompt(
            "hello world", ["yes", "no"], lambda value: value
        ).execute()
        self.assertEqual(result, "hello")


if __name__ == "__main__":
    unittest.main()
