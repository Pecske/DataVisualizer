from typing import Callable
from Section import Section
from SectionItem import SectionItem
from ItemName import ItemName


class RepetitionSection(Section):

    def __init__(self) -> None:
        super().__init__()

    def create_repetition_item(self) -> SectionItem:
        repetition_question: str = "Would you like to visualize another data point?"
        options: dict[int, str] = self.get_yes_no_options()
        evaluator: Callable = self.evaluate_repetition
        return SectionItem(
            ItemName.repetition,
            repetition_question,
            options,
            evaluator=evaluator,
            transformer=self.to_bold,
        )

    def evaluate_repetition(self, answer) -> bool:
        return answer == 2

    def proceed(self) -> None:
        if self.get_answer_by_item(ItemName.repetition):
            print("Exiting program. Goodbye!")
            exit()

    def init_items(self):
        super().init_items()
        self.add_item(ItemName.repetition, self.create_repetition_item())
