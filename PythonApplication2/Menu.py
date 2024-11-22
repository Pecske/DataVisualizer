from Page import Page


class Menu:

    def __init__(self, page: Page) -> None:
        self.page = page

    def __print_options(self, options: dict[int, str]) -> None:
        print("-------------------------")
        for k, v in options.items():
            print(f"[{k}]:{v}")
        print("-------------------------")

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

    def run_visualization_loop(self) -> None:
        while True:
            print("\033[H\033[3J", end="")  # ANSI escape code to clear console
            for section in self.page.sections:
                for item in section.items.values():
                    print(item.question)
                    options = item.get_printable_option()
                    self.__print_options(options)
                    answer = self.__get_user_input("Input: ", item.options)
                    item.store_user_answer(answer)

                section.proceed()
