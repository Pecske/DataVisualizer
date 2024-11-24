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
        action_page.add_section(ActivitySection(df))
        action_page.add_section(RepetitionSection())
        return action_page

    def build_page(self, page_name: PageName, df: DataFrame = None) -> Section:
        if page_name is PageName.activity:
            new_page = self.__build_activity_page(df)
        return new_page
