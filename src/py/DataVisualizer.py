from pandas import DataFrame
from FileReader import FileReader
from Menu import Menu
from PageBuilder import PageBuilder
from Page import Page
from PageName import PageName


def main():

    path = "../../src/data/stadat-ido0002-10.1.1.2-hu.csv"

    fileReader: FileReader = FileReader(path)
    df: DataFrame = fileReader.read_from_csv()

    builder: PageBuilder = PageBuilder()
    activity_page: Page = builder.build_page(PageName.activity, df)

    menu: Menu = Menu(activity_page)
    menu.run_visualization_loop()


# Main function entry
if __name__ == "__main__":
    main()
