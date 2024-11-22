from abc import abstractmethod
from ItemName import ItemName
from PageItem import PageItem


class Page:
    def __init__(self) -> None:
        self.items: dict[ItemName, PageItem] = dict()

    def add_item(self, item_name: ItemName, item: PageItem) -> None:
        self.items[item_name] = item

    @abstractmethod
    def proceed(self) -> None:
        pass
