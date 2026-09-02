from InquirerPrompt import inquirer


def main():
    """Multiline text prompt with optional external editor."""

    result = inquirer.text(
        message="Enter your notes:",
        multiline=True,
        open_in_editor=True,
        tempfile_suffix=".md",
    ).execute()

    print(f"Notes:\n{result}")


if __name__ == "__main__":
    main()
