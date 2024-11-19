from pandas import DataFrame
from Activity import Activity
from ActivityService import ActivityService
from FileReader import FileReader
from Menu import Menu

def main():

    path = "src/data/stadat-ido0002-10.1.1.2-hu.csv"

    fileReader: FileReader = FileReader(path)
    dataFrame: DataFrame = fileReader.read_from_csv()

    activityService: ActivityService = ActivityService()
    activities: dict[str, Activity] = activityService.convert_dataframe_to_activities(dataFrame)

    menu: Menu = Menu()
    menu.run_visualization_loop(activityService)

# Main function entry
if __name__ == "__main__":
    main()
