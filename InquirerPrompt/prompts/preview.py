"""Module contains the class to create a list prompt with a live preview pane."""

from typing import Any, Callable, List, Optional, Union

from prompt_toolkit.filters.cli import IsDone
from prompt_toolkit.formatted_text import (
    ANSI,
    HTML,
    FormattedText,
    StyleAndTextTuples,
    to_formatted_text,
)
from prompt_toolkit.layout.containers import ConditionalContainer, Container, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.dimension import Dimension

from InquirerPrompt.enum import INQUIRERPY_POINTER_SEQUENCE
from InquirerPrompt.exceptions import InvalidArgument
from InquirerPrompt.prompts.list import ListPrompt
from InquirerPrompt.utils import (
    InquirerPyDefault,
    InquirerPyKeybindings,
    InquirerPyListChoices,
    InquirerPyMessage,
    InquirerPySessionResult,
    InquirerPyStyle,
    InquirerPyValidate,
    calculate_height,
    rich_to_ansi,
)

__all__ = ["PreviewPrompt"]


def _is_rich_renderable(content: Any) -> bool:
    """Check if the content is a rich renderable.

    Plain strings and ``prompt_toolkit`` formatted text objects are not rich
    renderables; anything exposing rich's ``__rich_console__``/``__rich__``
    protocol is.
    """
    if isinstance(content, (str, HTML, ANSI, FormattedText)):
        return False
    return hasattr(content, "__rich_console__") or hasattr(content, "__rich__")


def format_preview_text(content: Any) -> StyleAndTextTuples:
    """Convert preview content into `prompt_toolkit` formatted text fragments.

    Supported content:

    - plain strings
    - `prompt_toolkit` formatted text objects (``HTML``, ``ANSI``,
      ``FormattedText``)
    - rich renderables (requires the optional ``rich`` extra)

    Args:
        content: The value returned by the ``preview`` callable.

    Returns:
        A list of ``(style, text)`` tuples.

    Raises:
        InvalidArgument: When a rich renderable is passed but the optional
            ``rich`` dependency is not installed.
    """
    if _is_rich_renderable(content):
        content = rich_to_ansi(content)
    return list(to_formatted_text(content))


class PreviewPrompt(ListPrompt):
    """Create a list prompt with a live preview pane for the highlighted choice.

    The ``preview`` callable is invoked with the value of the currently
    highlighted choice on every render and its return value is displayed in a
    pane below the choices. It may return a plain string, a
    `prompt_toolkit` formatted text object (``HTML``, ``ANSI``,
    ``FormattedText``) or a rich renderable (requires the optional ``rich``
    extra).

    A wrapper class around :class:`~prompt_toolkit.application.Application`.

    Args:
        message: The question to ask the user.
        choices: List of choices to display and select.
        preview: Callable invoked with the highlighted choice value, returning
            the preview content.
        preview_height: Preferred height of the preview pane. Accepts an int
            (exact lines) or a string percentage (e.g. ``"30%"``).
        preview_separator: Display a horizontal separator between the choices
            and the preview pane.
        default: Set the default value of the prompt.
        style: An :class:`InquirerPyStyle` instance.
        vi_mode: Use vim keybinding for the prompt.
        qmark: Question mark symbol.
        amark: Answer mark symbol.
        pointer: Pointer symbol.
        instruction: Short instruction to display next to the question.
        long_instruction: Long instructions to display at the bottom of the prompt.
        validate: Add validation to user input.
        invalid_message: Error message to display when user input is invalid.
        transformer: A function which performs additional transformation on the
            value that gets printed to the terminal.
        filter: A function which performs additional transformation on the result.
        height: Preferred height of the prompt.
        max_height: Max height of the prompt.
        multiselect: Enable multi-selection on choices.
        marker: Marker symbol used when `multiselect` is True.
        marker_pl: Marker place holder when the choice is not selected.
        border: Create border around the choice window.
        keybindings: Customise the builtin keybindings.
        show_cursor: Display cursor at the end of the prompt.
        cycle: Return to top item if hit bottom during navigation or vice versa.
        wrap_lines: Soft wrap question lines when question exceeds the terminal width.
        raise_keyboard_interrupt: Raise the :class:`KeyboardInterrupt` exception
            when `ctrl-c` is pressed.
        mandatory: Indicate if the prompt is mandatory.
        mandatory_message: Error message to show when user attempts to skip
            mandatory prompt.
        session_result: Used internally for classic syntax (PyInquirer).
        erase_when_done: Clear the rendered prompt from the terminal after the
            application exits.
        preview_height: Preferred height of the preview pane.

    Examples:
        >>> from InquirerPrompt import inquirer
        >>> result = inquirer.preview(
        ...     message="Select a fruit:",
        ...     choices=["apple", "banana"],
        ...     preview=lambda value: f"Selected: {value}",
        ... ).execute()
    """

    def __init__(
        self,
        message: InquirerPyMessage,
        choices: InquirerPyListChoices,
        preview: Callable[[Any], Any],
        default: InquirerPyDefault = None,
        style: Optional[InquirerPyStyle] = None,
        vi_mode: bool = False,
        qmark: str = "?",
        amark: str = "?",
        pointer: str = INQUIRERPY_POINTER_SEQUENCE,
        instruction: str = "",
        long_instruction: str = "",
        transformer: Optional[Callable[[Any], Any]] = None,
        filter: Optional[Callable[[Any], Any]] = None,
        height: Optional[Union[int, str]] = None,
        max_height: Optional[Union[int, str]] = None,
        multiselect: bool = False,
        marker: str = INQUIRERPY_POINTER_SEQUENCE,
        marker_pl: str = " ",
        border: bool = False,
        validate: Optional[InquirerPyValidate] = None,
        invalid_message: str = "Invalid input",
        keybindings: Optional[InquirerPyKeybindings] = None,
        show_cursor: bool = True,
        cycle: bool = True,
        wrap_lines: bool = True,
        raise_keyboard_interrupt: bool = True,
        mandatory: bool = True,
        mandatory_message: str = "Mandatory prompt",
        session_result: Optional[InquirerPySessionResult] = None,
        erase_when_done: bool = False,
        preview_height: Optional[Union[int, str]] = 6,
        preview_separator: bool = True,
    ) -> None:
        if not callable(preview):
            raise InvalidArgument(
                "preview must be a callable that accepts the highlighted choice value"
            )
        self._preview = preview
        self._preview_separator = preview_separator
        (
            self._dimmension_preview_height,
            self._dimmension_preview_max_height,
        ) = calculate_height(preview_height, None, height_offset=0)
        super().__init__(
            message=message,
            choices=choices,
            default=default,
            style=style,
            vi_mode=vi_mode,
            qmark=qmark,
            amark=amark,
            pointer=pointer,
            instruction=instruction,
            long_instruction=long_instruction,
            transformer=transformer,
            filter=filter,
            height=height,
            max_height=max_height,
            multiselect=multiselect,
            marker=marker,
            marker_pl=marker_pl,
            border=border,
            validate=validate,
            invalid_message=invalid_message,
            keybindings=keybindings,
            show_cursor=show_cursor,
            cycle=cycle,
            wrap_lines=wrap_lines,
            raise_keyboard_interrupt=raise_keyboard_interrupt,
            mandatory=mandatory,
            mandatory_message=mandatory_message,
            session_result=session_result,
            erase_when_done=erase_when_done,
        )

    def _get_preview_text(self) -> StyleAndTextTuples:
        """Obtain the preview content for the currently highlighted choice.

        Returns:
            FormattedText in list of tuple format.
        """
        try:
            value = self.content_control.selection["value"]
        except IndexError:
            return []
        try:
            content = self._preview(value)
        except Exception as e:  # noqa: BLE001 - preview is user provided code
            return [("class:skipped", "Preview error: %s" % e)]
        return format_preview_text(content)

    def _extra_content_containers(self) -> List[Container]:
        """Obtain the preview pane containers to render below the choices.

        Returns:
            A list of `prompt_toolkit` containers.
        """
        containers: List[Container] = []
        if self._preview_separator:
            containers.append(
                ConditionalContainer(
                    Window(
                        height=Dimension.exact(1),
                        char="─",
                        style="class:preview_separator",
                    ),
                    filter=~IsDone(),
                )
            )
        containers.append(
            ConditionalContainer(
                Window(
                    content=FormattedTextControl(
                        text=self._get_preview_text,
                        focusable=False,
                        show_cursor=False,
                    ),
                    height=Dimension(
                        min=1,
                        max=self._dimmension_preview_max_height,
                        preferred=self._dimmension_preview_height,
                    ),
                    wrap_lines=self._wrap_lines,
                    dont_extend_height=True,
                    style="class:preview",
                ),
                filter=~IsDone(),
            )
        )
        return containers
