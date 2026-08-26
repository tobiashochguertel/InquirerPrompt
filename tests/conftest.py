"""Pytest configuration for InquirerPy tests.

Patches prompt_toolkit's terminal I/O so tests that don't provide
their own input/output run successfully in CI (no real TTY available).
"""

import pytest


@pytest.fixture(autouse=True, scope="function")
def patch_terminal_for_tests():
    """Provide a fake pipe input/output session for all tests.

    Uses prompt_toolkit's ``create_app_session`` context manager to install
    a ``PipeInput`` and ``DummyOutput`` as the active terminal session.
    This avoids ``io.UnsupportedOperation: Stdin is not a terminal`` errors
    when running tests outside of a real TTY (e.g. CI).

    Tests that already pass ``input=`` to their prompts (e.g. test_secret,
    test_input, test_confirm, test_filepath) are unaffected; the Application
    constructor prefers the explicit input over the session default.
    """
    from prompt_toolkit.application.current import create_app_session
    from prompt_toolkit.input import create_pipe_input
    from prompt_toolkit.output import DummyOutput

    # create_pipe_input() returns a context manager in prompt_toolkit >= 3.0.40
    # — must use `with` to get the actual PipeInput object
    with create_pipe_input() as inp:
        with create_app_session(input=inp, output=DummyOutput()):
            yield inp
