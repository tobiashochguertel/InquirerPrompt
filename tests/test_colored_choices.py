"""Tests for colored choice names (HTML/ANSI/FormattedText support).

Verifies that choice names can be prompt_toolkit formatted text objects
(HTML, ANSI, FormattedText) and are correctly expanded into (style, text)
tuples by the prompt rendering methods.
"""
import unittest

from prompt_toolkit.formatted_text import ANSI, HTML, FormattedText

from InquirerPy.base.control import Choice
from InquirerPy.prompts.list import InquirerPyListControl, ListPrompt
from InquirerPy.prompts.checkbox import InquirerPyCheckboxControl
from InquirerPy.prompts.rawlist import InquirerPyRawlistControl
from InquirerPy.prompts.expand import InquirerPyExpandControl, ExpandPrompt, ExpandChoice, ExpandHelp
from InquirerPy.separator import Separator
from InquirerPy.utils import expand_formatted_text


class TestExpandFormattedText(unittest.TestCase):
    """Test the expand_formatted_text utility function."""

    def test_plain_string(self):
        """Plain strings are wrapped in a single (style, text) tuple."""
        result = expand_formatted_text("class:pointer", "hello")
        self.assertEqual(result, [("class:pointer", "hello")])

    def test_html(self):
        """HTML objects are expanded into (style, text) tuples."""
        result = expand_formatted_text("class:pointer", HTML("<ansigreen>✓ OK</ansigreen>"))
        self.assertEqual(
            result,
            [("class:ansigreen", "✓ OK")],
        )

    def test_html_multiple_tags(self):
        """HTML with multiple tags produces multiple tuples."""
        result = expand_formatted_text(
            "class:pointer",
            HTML("<ansigreen>Search: ✓</ansigreen>  <ansired>AI: ✗</ansired>"),
        )
        self.assertEqual(
            result,
            [
                ("class:ansigreen", "Search: ✓"),
                ("", "  "),
                ("class:ansired", "AI: ✗"),
            ],
        )

    def test_ansi(self):
        """ANSI objects are expanded into (style, text) tuples."""
        result = expand_formatted_text(
            "class:pointer", ANSI("\033[32mSearch: ✓\033[0m")
        )
        # ANSI parsing may produce per-character tuples; verify the text
        # content is correct and the style is ansigreen.
        full_text = "".join(t[1] for t in result)
        self.assertEqual(full_text, "Search: ✓")
        self.assertTrue(all(t[0] == "ansigreen" for t in result))

    def test_formatted_text(self):
        """FormattedText objects are passed through as lists of tuples."""
        ft = FormattedText(
            [("class:ansigreen", "yes"), ("", " "), ("class:ansired", "no")]
        )
        result = expand_formatted_text("class:pointer", ft)
        self.assertEqual(
            result,
            [("class:ansigreen", "yes"), ("", " "), ("class:ansired", "no")],
        )


class TestListPromptColoredChoices(unittest.TestCase):
    """Test colored choice names in ListPrompt."""

    def test_hover_text_with_html_name(self):
        """_get_hover_text expands HTML choice names."""
        control = InquirerPyListControl(
            [
                Choice("ok", name=HTML("<ansigreen>✓ OK</ansigreen>")),
                Choice("no", name=HTML("<ansired>✗ No</ansired>")),
            ],
            default="ok",
            pointer=">",
            marker=">",
            session_result=None,
            multiselect=False,
            marker_pl=" ",
        )
        hover = control._get_hover_text(control.choices[0])
        # Should contain the expanded HTML, not a raw HTML string
        styles = [t[0] for t in hover]
        texts = [t[1] for t in hover]
        self.assertIn("class:ansigreen", styles)
        self.assertIn("✓ OK", texts)
        # Should NOT contain the raw HTML tags
        self.assertFalse(any("<ansigreen>" in t for t in texts))

    def test_normal_text_with_html_name(self):
        """_get_normal_text expands HTML choice names."""
        control = InquirerPyListControl(
            [
                Choice("ok", name=HTML("<ansigreen>✓ OK</ansigreen>")),
                Choice("no", name=HTML("<ansired>✗ No</ansired>")),
            ],
            default="ok",
            pointer=">",
            marker=">",
            session_result=None,
            multiselect=False,
            marker_pl=" ",
        )
        normal = control._get_normal_text(control.choices[1])
        styles = [t[0] for t in normal]
        texts = [t[1] for t in normal]
        self.assertIn("class:ansired", styles)
        self.assertIn("✗ No", texts)
        self.assertFalse(any("<ansired>" in t for t in texts))

    def test_plain_string_still_works(self):
        """Plain string choice names work as before (backward compat)."""
        control = InquirerPyListControl(
            ["yes", "no"],
            default="yes",
            pointer=">",
            marker=">",
            session_result=None,
            multiselect=False,
            marker_pl=" ",
        )
        hover = control._get_hover_text(control.choices[0])
        self.assertIn(("class:pointer", "yes"), hover)

        normal = control._get_normal_text(control.choices[1])
        self.assertIn(("", "no"), normal)

    def test_separator_with_plain_name(self):
        """Separator names work as before (plain strings)."""
        control = InquirerPyListControl(
            [Separator("--- Section ---"), "yes"],
            default="yes",
            pointer=">",
            marker=">",
            session_result=None,
            multiselect=False,
            marker_pl=" ",
        )
        normal = control._get_normal_text(control.choices[0])
        self.assertIn(("class:separator", "--- Section ---"), normal)


class TestCheckboxPromptColoredChoices(unittest.TestCase):
    """Test colored choice names in CheckboxPrompt."""

    def test_hover_text_with_html_name(self):
        control = InquirerPyCheckboxControl(
            [
                Choice("ok", name=HTML("<ansigreen>✓ OK</ansigreen>")),
                Choice("no", name=HTML("<ansired>✗ No</ansired>")),
            ],
            default="ok",
            pointer=">",
            enabled_symbol="[x]",
            disabled_symbol="[ ]",
            session_result=None,
        )
        hover = control._get_hover_text(control.choices[0])
        styles = [t[0] for t in hover]
        texts = [t[1] for t in hover]
        self.assertIn("class:ansigreen", styles)
        self.assertIn("✓ OK", texts)


class TestRawlistPromptColoredChoices(unittest.TestCase):
    """Test colored choice names in RawlistPrompt."""

    def test_hover_text_with_html_name(self):
        control = InquirerPyRawlistControl(
            [
                Choice("ok", name=HTML("<ansigreen>✓ OK</ansigreen>")),
                Choice("no", name=HTML("<ansired>✗ No</ansired>")),
            ],
            default=1,
            pointer=">",
            separator=") ",
            marker=">",
            session_result=None,
            multiselect=False,
            marker_pl=" ",
        )
        hover = control._get_hover_text(control.choices[0])
        styles = [t[0] for t in hover]
        texts = [t[1] for t in hover]
        self.assertIn("class:ansigreen", styles)
        self.assertIn("✓ OK", texts)


class TestExpandPromptColoredChoices(unittest.TestCase):
    """Test colored choice names in ExpandPrompt."""

    def test_hover_text_with_html_name(self):
        control = InquirerPyExpandControl(
            [
                ExpandChoice("ok", name=HTML("<ansigreen>✓ OK</ansigreen>"), key="o"),
                ExpandChoice("no", name=HTML("<ansired>✗ No</ansired>"), key="n"),
            ],
            default="o",
            pointer=">",
            separator=") ",
            expand_help=ExpandHelp(),
            expand_pointer=">",
            marker=">",
            session_result=None,
            multiselect=False,
            marker_pl=" ",
        )
        hover = control._get_hover_text(control.choices[0])
        styles = [t[0] for t in hover]
        texts = [t[1] for t in hover]
        self.assertIn("class:ansigreen", styles)
        self.assertIn("✓ OK", texts)


class TestChoiceDataclass(unittest.TestCase):
    """Test that Choice accepts non-string names."""

    def test_choice_with_html_name(self):
        c = Choice("value", name=HTML("<ansigreen>green</ansigreen>"))
        self.assertIsInstance(c.name, HTML)

    def test_choice_with_ansi_name(self):
        c = Choice("value", name=ANSI("\033[32mgreen\033[0m"))
        self.assertIsInstance(c.name, ANSI)

    def test_choice_with_formatted_text_name(self):
        ft = FormattedText([("class:ansigreen", "green")])
        c = Choice("value", name=ft)
        self.assertIsInstance(c.name, FormattedText)

    def test_choice_with_plain_string_name(self):
        c = Choice("value", name="plain")
        self.assertEqual(c.name, "plain")

    def test_choice_name_defaults_to_str_value(self):
        c = Choice(42)
        self.assertEqual(c.name, "42")


if __name__ == "__main__":
    unittest.main()
