from pandas import DataFrame
from Page import Page
from Section import Section
from ActivitySection import ActivitySection
from ItemName import ItemName
from PageName import PageName
from RepetitionSection import RepetitionSection


class PageBuilder:

    def __build_activity_page(self, df: DataFrame) -> Page:
        action_page: Page = Page()
        action_page.add_section(self.__build_activity(df))
        action_page.add_section(self.__build_repetition())
        return action_page

    def __build_activity(self, df: DataFrame) -> ActivitySection:
        activity_section: ActivitySection = ActivitySection(df)
        activity_section.add_item(
            ItemName.activity, activity_section.create_activity_item()
        )
        activity_section.add_item(
            ItemName.linear, activity_section.create_linear_regression_item()
        )
        activity_section.add_item(
            ItemName.filter, activity_section.create_filter_item()
        )

        return activity_section

    def __build_repetition(self) -> RepetitionSection:
        repetition_section: RepetitionSection = RepetitionSection()
        repetition_section.add_item(
            ItemName.repetition, repetition_section.create_repetition_item()
        )

        return repetition_section

    def build_page(self, page_name: PageName, df: DataFrame = None) -> Section:
        if page_name is PageName.activity:
            new_page = self.__build_activity_page(df)
        return new_page
