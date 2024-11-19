from pandas import DataFrame
from Activity import Activity
from ActivityService import ActivityService
from FileReader import FileReader
from Menu import Menu

path = "src/data/stadat-ido0002-10.1.1.2-hu.csv"

fileReader : FileReader = FileReader(path)
dataFrame : DataFrame = fileReader.read_from_csv()

activityService : ActivityService = ActivityService()
activities : dict[str,Activity] = activityService.convert_dataframe_to_activities(dataFrame)

menu : Menu = Menu()

chosenCategory : str = menu.get_chosen_category(activityService.get_activity_names())
isLinear : bool = menu.is_linear_regression_shown()
activityService.showPlot(chosenCategory, isLinear)
