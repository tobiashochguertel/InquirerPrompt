# patched_print

```{note}
Printing values while the prompt is running can cause various side effects. Using the patched print function from
`InquirerPrompt` can print the value above the prompt without causing side effects. Mostly useful for debugging.
```

`InquirerPrompt` provides a helper function {func}`~InquirerPy.utils.patched_print` which can help printing to the terminal
while the prompt is still running.

```{eval-rst}
.. autofunction:: InquirerPy.utils.patched_print
    :noindex:
```

The following example will print "Hello World" above the prompt when `alt-b` is pressed.

```python
from InquirerPrompt.utils import patched_print
from InquirerPrompt import inquirer

prompt = inquirer.text(message="Name:")

@prompt.register_kb("alt-b")
def _(_):
    patched_print("Hello World")

name = prompt.execute()
```
