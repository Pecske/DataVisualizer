from collections.abc import Callable
from ActivityService import ActivityService


class Menu:

    def __init__(self, activity_service: ActivityService) -> None:
        self.activity_service = activity_service
        self.filter_method: dict[str, Callable] = {
            1: self.activity_service.show_activity,
            2: self.activity_service.show_activity_plot_by_gender,
        }

    def __print_options(self, options: dict[int, str]) -> None:
        mainCategory = [
            1,
            2,
            5,
            8,
            17,
            19,
            23,
            24,
            28,
            41,
            42,
            43,
        ]  # Index of all main category data points
        print("-------------------------")
        for k, v in options.items():

            if k < 10:  # Single digit case
                base_spacing = "  "
            else:  # Double digit case
                base_spacing = " "

            # Add extra spacing for non-main categories
            if k not in mainCategory:  # Non-main categories
                additional_spacing = " "
                prefix = "↪ "
            else:
                additional_spacing = ""
                prefix = ""

            # Special case for item 34
            if k == 34:
                additional_spacing += "    "
                prefix = "↪ "

            # Combine all spacings
            spaces_after_colon = base_spacing + additional_spacing

            # Apply bold and uppercase for mainCategory items, and capitalize for others
            if k in mainCategory:
                print(
                    f"[{k}]:{spaces_after_colon}\033[1m{v.upper()}\033[0m"
                )  # Bold and upper
            else:
                print(
                    f"[{k}]:{spaces_after_colon}{prefix}{v.capitalize()}"
                )  # Capitalize for others
        print("-------------------------")

    def __create_options_from_names(self, optionNames: list[str]) -> dict[int, str]:
        options: dict[int, str] = dict()
        index: int = 1
        for optionName in optionNames:
            options[index] = optionName
            index += 1
        return options

    def __get_user_input(
        self, prompt: str, options: dict[int, str] = None
    ) -> str | int:
        """
        Unified input-checking method. Handles numeric input for options or allows freeform strings.
        Detects 'q' or 'quit' for exiting the program.
        """
        while True:
            user_input = input(prompt).strip().lower()

            if user_input in ["q", "quit"]:
                print("Exiting program. Goodbye!")
                exit()

            if options:
                if user_input.isdigit() and int(user_input) in options:
                    return int(user_input)  # Return numeric key if valid
                else:
                    print("Invalid input. Please choose a valid option.")
            else:
                return user_input  # Return raw string for freeform input

    def get_chosen_category(self, optionNames: list[str]) -> str:
        options: dict[int, str] = self.__create_options_from_names(optionNames)
        print(
            "Choose an activity to be shown (press the number associated with it):\nTo exit the program type (q or quit)"
        )
        self.__print_options(options)
        return options[self.__get_user_input("Input: ", options)].strip()

    def is_linear_regression_shown(self) -> bool:
        options: dict[int, str] = {1: "Yes", 2: "No"}
        print("Do you want linear regression to be shown?")
        self.__print_options(options)
        chosen_key = self.__get_user_input("Input: ", options)
        return chosen_key == 1  # Convert numeric key to boolean

    def choose_filter(self) -> int:
        options: dict[int, str] = {1: "All", 2: "By Gender"}
        print("Apply a filter: ")
        self.__print_options(options)
        return self.__get_user_input("Input: ", options)

    def run_visualization_loop(self) -> None:
        while True:
            print("\033[H\033[3J", end="")  # ANSI escape code to clear console
            chosen_category = self.get_chosen_category(
                self.activity_service.get_activity_names()
            )
            show_linear = self.is_linear_regression_shown()
            activity_filter: int = self.choose_filter()
            self.filter_method[activity_filter](chosen_category, show_linear)

            # Check if the user wants to continue
            options: dict[int, str] = {1: "Yes", 2: "No"}
            print("Would you like to visualize another data point?")
            self.__print_options(options)

            continue_choice = self.__get_user_input("Input: ", options)
            if continue_choice == 2:
                print("Exiting program. Goodbye!")
                break
