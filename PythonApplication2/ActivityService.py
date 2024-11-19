from pandas import DataFrame
from Activity import Activity
import matplotlib.pyplot as plt
import numpy as np


class ActivityService:
    def __init__(self) -> None:
        self.activityDict : dict[str,Activity] = {}

    def __get_linear_regression_values(self,xValues : list[int], yValues : list[int]) -> np.poly1d:
        coef = np.polyfit(xValues,yValues,1)
        return np.poly1d(coef)

    def __map_columns_to_ints(self,columnNames : list[str]) -> list[int]:
        newIndex : int = 0
        columnValues : dict[str,int] = {}
        for name in columnNames:
            if(name not in columnValues):
                columnValues[name] = newIndex
                newIndex+=1
        return list(columnValues.values())

    def convert_dataframe_to_activities(self,df : DataFrame) -> dict[str,Activity] :
        dfDict : dict[str,int] = df.set_index(df.columns[0]).T.to_dict("list")

        for k,v in dfDict.items():
            newActivity : Activity = Activity(k)
            columnIndex : int = 1
            for value in v:
                newActivity.add_subGroup(str(df.columns[columnIndex]),int(value))
                columnIndex = columnIndex + 1
            if(k not in self.activityDict):
                self.activityDict[k] = newActivity
            if(k[0].isupper()):
                currentParent = k
            if(k[0].islower() and currentParent in self.activityDict):
                parent : Activity = self.activityDict.get(currentParent)
                parent.add_activity(newActivity)
        return self.activityDict

    def get_activities(self) -> dict[str,Activity]:
        return self.activityDict

    def showPlot(self,activityName : str, showLinear : bool) -> None:
        if(activityName in self.activityDict):
            currentActivity : Activity = self.activityDict.get(activityName)
            x : list[str] = list(currentActivity.timeValueDict.keys())
            y : list[int] = list(currentActivity.timeValueDict.values())
            plt.figure(activityName)
            plt.title(activityName)
            plt.plot(x,y)
            plt.ylabel = currentActivity.name
            plt.tight_layout()
            if(showLinear == True):
                newIndex : int = 0
                regression : dict[str,int] = {}
                for time in x:
                    if(time not in regression):
                        regression[time] = newIndex
                        newIndex+=1
                regressionX : list[int] = self.__map_columns_to_ints(x)
                poly : np.poly1d = self.__get_linear_regression_values(regressionX,y)                
                plt.plot(regressionX,poly(regressionX))
            plt.show()

    def get_activity_names(self) -> list[str]:
        return list(self.activityDict.keys())
