#!/usr/bin/env python3
"""Manual test script for colored choice names in InquirerPy.

Demonstrates HTML and ANSI formatted text as choice names across
all list-type prompts: select, checkbox, rawlist, expand, fuzzy.

Run in a terminal:
    python examples/colored_choices.py
"""
from prompt_toolkit.formatted_text import HTML, ANSI

from InquirerPrompt import inquirer
from InquirerPrompt.base.control import Choice
from InquirerPrompt.separator import Separator


def test_select():
    """ListPrompt (select) with colored choices."""
    print("\n=== select (HTML) ===")
    result = inquirer.select(
        message="Select a shell:",
        choices=[
            Choice("zsh", name=HTML("<ansibrightcyan>Zsh</ansibrightcyan>  <ansigreen>Search: ✓</ansigreen>  <ansigreen>AI: ✓</ansigreen>")),
            Choice("bash", name=HTML("<ansibrightcyan>Bash</ansibrightcyan>  <ansigreen>Search: ✓</ansigreen>  <ansigreen>AI: ✓</ansigreen>")),
            Choice("fish", name=HTML("<ansibrightcyan>Fish</ansibrightcyan>  <ansired>Search: ✗</ansired>  <ansired>AI: ✗</ansired>")),
            Separator(),
            Choice("nu", name=HTML("<ansibrightcyan>Nushell</ansibrightcyan>  <ansigreen>Search: ✓</ansigreen>  <ansiyellow>AI: n/a</ansiyellow>")),
            Choice("exit", name=HTML("<ansibrightblack>Exit</ansibrightblack>")),
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


def test_select_ansi():
    """ListPrompt (select) with ANSI colored choices."""
    print("\n=== select (ANSI) ===")
    result = inquirer.select(
        message="Select a color:",
        choices=[
            Choice("red", name=ANSI("\033[31m● Red\033[0m")),
            Choice("green", name=ANSI("\033[32m● Green\033[0m")),
            Choice("blue", name=ANSI("\033[34m● Blue\033[0m")),
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


def test_checkbox():
    """CheckboxPrompt with colored choices."""
    print("\n=== checkbox (HTML) ===")
    result = inquirer.checkbox(
        message="Select features:",
        choices=[
            Choice("search", name=HTML("<ansigreen>✓ Search</ansigreen>")),
            Choice("ai", name=HTML("<ansigreen>✓ AI</ansigreen>")),
            Choice("sync", name=HTML("<ansiyellow>? Sync (beta)</ansiyellow>")),
            Choice("telemetry", name=HTML("<ansired>✗ Telemetry</ansired>")),
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


def test_rawlist():
    """RawlistPrompt with colored choices."""
    print("\n=== rawlist (HTML) ===")
    result = inquirer.rawlist(
        message="Select an option:",
        choices=[
            Choice("ok", name=HTML("<ansigreen>✓ OK</ansigreen>")),
            Choice("warn", name=HTML("<ansiyellow>⚠ Warning</ansiyellow>")),
            Choice("err", name=HTML("<ansired>✗ Error</ansired>")),
        ],
    ).execute()
    print(f"Selected: {result}")


def test_expand():
    """ExpandPrompt with colored choices."""
    print("\n=== expand (HTML) ===")
    result = inquirer.expand(
        message="Select a status:",
        choices=[
            Choice("ok", name=HTML("<ansigreen>✓ OK</ansigreen>"), key="o"),
            Choice("warn", name=HTML("<ansiyellow>⚠ Warning</ansiyellow>"), key="w"),
            Choice("err", name=HTML("<ansired>✗ Error</ansired>"), key="e"),
        ],
    ).execute()
    print(f"Selected: {result}")


def test_fuzzy():
    """FuzzyPrompt with colored choices."""
    print("\n=== fuzzy (HTML) ===")
    result = inquirer.fuzzy(
        message="Search a fruit:",
        choices=[
            Choice("apple", name=HTML("<ansired>🍎 Apple</ansired>")),
            Choice("banana", name=HTML("<ansiyellow>🍌 Banana</ansiyellow>")),
            Choice("grape", name=HTML("<ansibrightmagenta>🍇 Grape</ansibrightmagenta>")),
            Choice("kiwi", name=HTML("<ansigreen>🥝 Kiwi</ansigreen>")),
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


def test_mixed():
    """ListPrompt with mixed plain and colored choices."""
    print("\n=== select (mixed plain + HTML) ===")
    result = inquirer.select(
        message="Mixed choices:",
        choices=[
            "plain string",
            Choice("html", name=HTML("<ansigreen>HTML colored</ansigreen>")),
            Choice("ansi", name=ANSI("\033[36mANSI colored\033[0m")),
            "another plain",
        ],
        border=True,
    ).execute()
    print(f"Selected: {result}")


if __name__ == "__main__":
    print("InquirerPy Colored Choices Demo")
    print("=" * 40)
    test_select()
    test_select_ansi()
    test_mixed()
    test_checkbox()
    test_rawlist()
    test_expand()
    test_fuzzy()
    print("\n✓ All demos complete!")
