"""Servers as another entry point for `InquirerPy`.

See Also:
    :ref:`index:Alternate Syntax`.

`inquirer` directly interact with individual prompt classes. It’s more flexible, easier to customise and also provides IDE type hintings/completions.
"""

__all__ = [
    "checkbox",
    "confirm",
    "expand",
    "filepath",
    "fuzzy",
    "text",
    "select",
    "number",
    "rawlist",
    "secret",
]

from InquirerPrompt.prompts import CheckboxPrompt as checkbox
from InquirerPrompt.prompts import ConfirmPrompt as confirm
from InquirerPrompt.prompts import ExpandPrompt as expand
from InquirerPrompt.prompts import FilePathPrompt as filepath
from InquirerPrompt.prompts import FuzzyPrompt as fuzzy
from InquirerPrompt.prompts import InputPrompt as text
from InquirerPrompt.prompts import ListPrompt as select
from InquirerPrompt.prompts import NumberPrompt as number
from InquirerPrompt.prompts import RawlistPrompt as rawlist
from InquirerPrompt.prompts import SecretPrompt as secret
