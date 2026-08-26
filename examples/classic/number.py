from InquirerPrompt import prompt
from InquirerPrompt.validator import EmptyInputValidator


def main() -> None:
    questions = [
        {
            "type": "number",
            "message": "Enter integer:",
            "min_allowed": -2,
            "max_allowed": 10,
            "validate": EmptyInputValidator(),
        },
        {
            "type": "number",
            "message": "Enter float:",
            "float_allowed": True,
            "validate": EmptyInputValidator(),
        },
    ]

    result = prompt(questions)


if __name__ == "__main__":
    main()
