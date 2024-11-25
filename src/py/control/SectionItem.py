from collections.abc import Callable
from typing import Any
from utils.ItemName import ItemName


class SectionItem:
    def __init__(
        self,
        item_name: ItemName,
        question: str,
        options: dict[int, str],
        evaluator: Callable = None,
        transformer: Callable = None,
    ) -> None:
        self.item_name: ItemName = item_name
        self.question = question
        self.options = options
        self.evaluator = evaluator
        if transformer is not None:
            self.printable_options: dict[int, str] = transformer(self.options)

    def store_user_answer(self, answer: str | int) -> None:
        if self.evaluator is None:
            self.user_answer = self.get_option_by_index(answer)
        else:
            self.user_answer = self.evaluator(answer)

    def get_printable_option(self) -> dict[int, str]:
        if self.printable_options is not None:
            result = self.printable_options
        else:
            result = self.options
        return result

    def get_option_by_index(self, index: int) -> str:
        return self.options.get(index)

    def get_answer(self) -> Any:
        return self.user_answer
