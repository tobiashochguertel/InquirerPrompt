from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from InquirerPrompt import inquirer

PACKAGES = {
    "inquirerprompt": {"version": "0.5.0", "license": "MIT", "size": "48 kB"},
    "prompt-toolkit": {"version": "3.0.53", "license": "BSD-3", "size": "420 kB"},
    "pfzy": {"version": "0.3.4", "license": "MIT", "size": "12 kB"},
    "rich": {"version": "14.0.0", "license": "MIT", "size": "1.2 MB"},
}


def render_package(value):
    info = PACKAGES[value]
    table = Text.assemble(
        ("Version  ", "bold"),
        (info["version"], "green"),
        "\n",
        ("License  ", "bold"),
        info["license"],
        "\n",
        ("Size     ", "bold"),
        info["size"],
    )
    return Panel(
        Group(table),
        title=value,
        border_style="green",
        expand=False,
    )


def main():
    value = inquirer.preview(
        message="Select a package:",
        choices=list(PACKAGES),
        preview=render_package,
        border=True,
        preview_height=7,
    ).execute()
    print("Selected: %s" % value)


if __name__ == "__main__":
    main()
