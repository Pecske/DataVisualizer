from pandas import DataFrame
from Page import Page
from ActivityPage import ActivityPage
from ItemName import ItemName
from PageName import PageName


class PageBuilder:

    def build_page(self, page_name: PageName, df: DataFrame) -> Page:
        if page_name == PageName.activity:
            new_page = ActivityPage.build_activity()

        return new_page

    def build_activity(self, df: DataFrame) -> ActivityPage:
        page: ActivityPage = ActivityPage(df)
        page.add_item(ItemName.activity, page.create_activity_item())
        page.add_item(ItemName.linear, page.create_linear_regression_item())
        page.add_item(ItemName.filter, page.create_filter_item())

        return page
