# preview

A prompt that displays a list of choices with a live preview pane for the
highlighted choice. The preview updates as you move through the choices.

## Example

<details open>
  <summary>Alternate Syntax</summary>

```{eval-rst}
.. literalinclude :: ../../../examples/alternate/preview.py
   :language: python
```

</details>

## Preview callable

`preview` is called with the **value** of the currently highlighted choice on
every render. It may return:

- a plain string,
- a `prompt_toolkit` formatted text object (`HTML`, `ANSI`, `FormattedText`),
- a `rich` renderable — requires the optional extra:

```sh
pip install "InquirerPrompt[rich]"
```

```python
from rich.panel import Panel

from InquirerPrompt import inquirer


def render_preview(value):
    return Panel(f"Details for {value}", border_style="green")


result = inquirer.preview(
    message="Select an option:",
    choices=["one", "two", "three"],
    preview=render_preview,
    preview_height=7,
).execute()
```

If the callable raises, the error is rendered inside the preview pane instead
of crashing the prompt.

## Layout

- `preview_height`: preferred height of the preview pane. Accepts an int
  (exact lines) or a string percentage (e.g. `"30%"`). Defaults to `6`.
- `preview_separator`: draw a horizontal separator between the choices and the
  preview pane. Defaults to `True`. The separator uses the `preview_separator`
  style class.

## Keybindings

```{seealso}
{ref}`pages/prompts/list:Keybindings`
```

All keybindings of the {ref}`list prompt <pages/prompts/list:select>` apply.
