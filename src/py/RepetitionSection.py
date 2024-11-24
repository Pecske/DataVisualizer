from Section import Section
from SectionItem import SectionItem
from ItemName import ItemName


class RepetitionSection(Section):

    def __init__(self) -> None:
        super().__init__()

    def create_repetition_item(self) -> SectionItem:
        repetition_question: str = "Would you like to visualize another data point?"
        options: dict[int, str] = self.get_yes_no_options()
        return SectionItem(repetition_question, options, self.to_bold)

    def proceed(self) -> None:
        repetition_answer: bool = self.items[ItemName.repetition].user_answer == 2
        if repetition_answer:
            print("Exiting program. Goodbye!")
            exit()

    def init_items(self):
        super().init_items()
        self.add_item(ItemName.repetition, self.create_repetition_item())
