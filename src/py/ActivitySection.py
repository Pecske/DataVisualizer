from typing import Any, Callable
from pandas import DataFrame
from ActivityService import ActivityService
from ItemName import ItemName
from Section import Section
from SectionItem import SectionItem
from GenderName import GenderName
from TableData import TableData


class ActivitySection(Section):

    def __init__(self, df: DataFrame) -> None:
        self.activity_service: ActivityService = ActivityService(df)
        super().__init__()
        self.gender_answer_map: dict[int, list[GenderName]] = {1: [GenderName.all]}

    def proceed(self) -> None:
        filters: dict[ItemName, Any] = dict()
        for k, v in self.items.items():
            filters[k] = v.user_answer
        data: TableData = self.activity_service.map_base_data_to_table(filters)
        self.activity_service.show_plot(data)

    def init_items(self) -> None:
        super().init_items()
        self.add_item(ItemName.activity, self.create_activity_item())
        self.add_item(ItemName.linear, self.create_linear_regression_item())
        self.add_item(ItemName.gender, self.create_gender_item())

    def get_activity_options(self, options: dict[int, str]) -> dict[int, str]:
        result: dict[int, str] = dict()
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
                result[k] = (
                    f"{spaces_after_colon}\033[1m{v.upper()}\033[0m"  # Bold and upper
                )
            else:
                result[k] = (
                    f"{spaces_after_colon}{prefix}{v.capitalize()}"  # Capitalize for others
                )
        return result

    def get_gender_filter_options(self) -> dict[int, str]:
        return {1: "All", 2: "By Gender"}

    def __create_options_from_names(self, optionNames: list[str]) -> dict[int, str]:
        options: dict[int, str] = dict()
        index: int = 1
        for optionName in optionNames:
            options[index] = optionName
            index += 1
        return options

    def create_activity_item(self) -> SectionItem:
        activity_question: str = (
            "Choose an activity to be shown (press the number associated with it):\nTo exit the program type (q or quit)"
        )
        activity_names: list[str] = self.activity_service.get_activity_names()
        options: dict[int, str] = self.__create_options_from_names(activity_names)
        return SectionItem(
            ItemName.activity,
            activity_question,
            options,
            transformer=self.get_activity_options,
        )

    def create_linear_regression_item(self) -> SectionItem:
        linear_regression_question: str = "Do you want linear regression to be shown?"
        options: dict[int, str] = self.get_yes_no_options()
        evaluator: Callable = self.evaluate_linear
        return SectionItem(
            ItemName.linear,
            linear_regression_question,
            options,
            evaluator=evaluator,
            transformer=self.to_bold,
        )

    def create_gender_item(self) -> SectionItem:
        filter_question: str = "Apply a gender filter: "
        options: dict[int, str] = self.get_gender_filter_options()
        evaluator: Callable = self.evaluate_gender
        return SectionItem(
            ItemName.gender,
            filter_question,
            options,
            evaluator=evaluator,
            transformer=self.to_bold,
        )

    def evaluate_linear(self, answer) -> bool:
        return answer == 1

    def evaluate_gender(self, answer) -> list[GenderName]:
        return self.gender_answer_map.get(answer)
