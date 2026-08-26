# FAQ

## Can I change how the user answer is displayed?

```{seealso}
{ref}`pages/dynamic:transformer`
```

Yes, especially for list type prompts with multiple selection, printing selection
as a list is not ideal in a lot of scenarios. Use `transformer` parameter to customise it.

## How can I do unittest when using `InquirerPrompt`?

```{tip}
Since `InquirerPrompt` module itself is tested, there's no need to mock any futher/deeper than the API entrypoint (`prompt` and `inquirer`).
```

For {ref}`index:Classic Syntax (PyInquirer)` user, it would be just a direct mock on the {ref}`pages/prompt:prompt` function.

```{code-block} python
---
caption: Module/somefunction.py
---
from InquirerPrompt import prompt

def get_name():
    return prompt({"type": "input", "message": "Name:"})
```

```{code-block} python
---
caption: tests/test_somefunction.py
---
import unittest
from unittest.mock import patch

from Module.somefunction import get_name

class TestPrompt(unittest.TestCase):
    @patch("Module.somefunction.prompt")
    def test_get_name(self, mocked_prompt):
        mocked_prompt.return_value = "hello"
        result = get_name()
        self.assertEqual(result, "hello")
```

For {ref}`index:Alternate Syntax` user, you'd have to mock 1 level deeper to the prompt class level.

```{code-block} python
---
caption: Module/somefunction.py
---
from InquirerPrompt import inquirer

def get_name():
    return inquirer.text(message="Name:").execute()
```

```{code-block} python
---
caption: tests/test_somefunction.py
---
import unittest
from unittest.mock import patch

from Module.somefunction import get_name

class TestPrompt(unittest.TestCase):
    @patch("Module.somefunction.inquirer.text")
    def test_get_name(self, mocked_prompt):
        mocked_prompt.return_value = "hello"
        result = get_name()
        self.assertEqual(result, "hello")
```

## Can I navigate back to the previous question?

No. With the current implementation this is not possible since the control of the prompt is terminated after it is answered.
This may be supported in the future but not a priority at the moment.

## Is InquirerPrompt compatible with kazhala/InquirerPy (upstream)?

**Yes — InquirerPrompt is designed to be a drop-in replacement for the upstream `InquirerPy` package.**

The import name has changed from `import InquirerPy` to `import InquirerPrompt`.
Replace your `pip install InquirerPy` with `pip install InquirerPrompt` and update your imports
from `from InquirerPy import ...` to `from InquirerPrompt import ...`. All public APIs are otherwise unchanged.

```sh
# Before (upstream, now unmaintained)
pip install InquirerPy

# After (this fork, actively maintained)
pip install InquirerPrompt
```

```python
# Update your imports — everything else stays the same
from InquirerPrompt import prompt, inquirer
```

Our goal is to maintain **full backwards-compatibility** with upstream `InquirerPy 0.3.4` (the last upstream release) for as long as possible.
Any intentional API changes will be clearly documented in the [changelog](changelog.md) and in the [Compatibility Report](compatibility.md).

See the [Compatibility Report](compatibility.md) for a detailed API surface comparison between this fork and the upstream release.
