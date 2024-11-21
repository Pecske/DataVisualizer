import os
from pandas import DataFrame
from Activity import Activity
from ActivityService import ActivityService
from FileReader import FileReader
from Menu import Menu


def main():

    path = os.getcwd()+"\\PythonApplication2\\src\\data\\stadat-ido0002-10.1.1.2-hu.csv"


    fileReader: FileReader = FileReader(path)
    df: DataFrame = fileReader.read_from_csv()

    activity_service: ActivityService = ActivityService(df)

    menu: Menu = Menu(activity_service)
    menu.run_visualization_loop()


# Main function entry
if __name__ == "__main__":
    main()
