from collections.abc import Callable


class PageItem:
    def __init__(
        self, question: str, options: dict[int, str], transformer: Callable = None
    ) -> None:
        self.question = question
        self.options = options
        if transformer is not None:
            self.printable_options: dict[int, str] = transformer(self.options)

    def store_user_answer(self, answer: str | int) -> None:
        self.user_answer = answer

    def get_printable_option(self) -> dict[int, str]:
        if self.printable_options is not None:
            result = self.printable_options
        else:
            result = self.options
        return result

    def get_option_by_index(self, index: int) -> str:
        return self.options.get(index)
