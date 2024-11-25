from pandas import DataFrame
from utils.FileReader import FileReader
from control.Menu import Menu
from utils.PageBuilder import PageBuilder
from control.Page import Page
from utils.PageName import PageName


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
