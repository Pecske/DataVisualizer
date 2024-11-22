from pandas import DataFrame
from Activity import Activity
import matplotlib.pyplot as plt
import numpy as np
from TableData import TableData


class ActivityService:
    def __init__(self, df: DataFrame) -> None:
        self.activities: dict[str, Activity] = self.convert_dataframe_to_activities(df)

    def __get_linear_regression_values(
        self, xValues: list[int], yValues: list[int]
    ) -> np.poly1d:
        coef = np.polyfit(xValues, yValues, 1)
        return np.poly1d(coef)

    def __map_columns_to_ints(self, column_names: list[str]) -> list[int]:
        new_index: int = 0
        column_values: dict[str, int] = dict()
        for name in column_names:
            if name not in column_values:
                column_values[name] = new_index
                new_index += 1
        return list(column_values.values())

    def convert_dataframe_to_activities(self, df: DataFrame) -> dict[str, Activity]:
        rotated_data_frame: dict[str, int] = df.set_index(df.columns[0]).T.to_dict(
            "list"
        )
        activities: dict[str, Activity] = dict()
        for k, v in rotated_data_frame.items():
            new_activity: Activity = Activity(k)
            column_index: int = 1
            for value in v:
                new_activity.add_sub_group(str(df.columns[column_index]), int(value))
                column_index = column_index + 1
            if k not in activities:
                activities[k] = new_activity
            if k[0].isupper():
                current_parent = k
            if k[0].islower() and current_parent in activities:
                parent: Activity = activities.get(current_parent)
                parent.add_activity(new_activity)
        return activities

    def get_activities(self) -> dict[str, Activity]:
        return self.activities

    def show_plot(self, table_data: TableData) -> None:
        plt.figure(table_data.name.capitalize())
        plt.title(table_data.name.capitalize())
        plt.tight_layout()
        plt.ylabel("Fő / Perc")
        plt.style.use("fivethirtyeight")
        for yValues in table_data.y:
            plt.plot(table_data.x, yValues)
            if table_data.isLinear:
                dummyX: list[int] = self.__map_columns_to_ints(table_data.x)
                poly: np.poly1d = self.__get_linear_regression_values(dummyX, yValues)
                plt.plot(dummyX, poly(dummyX))
        if table_data.legend is not None and len(table_data.legend) > 0:
            plt.legend(table_data.legend)
        plt.show()

    def show_activity(self, activity_name: str, show_linear: bool) -> None:
        if activity_name in self.activities:
            current_activity: Activity = self.activities.get(activity_name)
            x: list[str] = list(current_activity.time_values.keys())
            y: list[int] = list(current_activity.time_values.values())
            yValues: list[list[int]] = list()
            yValues.append(y)
            table_data: TableData = TableData(x, yValues, activity_name, show_linear)
            self.show_plot(table_data)

    def show_activity_plot_by_gender(
        self, activity_name: str, show_linear: bool
    ) -> None:
        if activity_name in self.activities:
            current_activity: Activity = self.activities.get(activity_name)
            gender_times: dict[str, dict[str, int]] = (
                current_activity.get_group_by_gender()
            )
            x: list[str] = current_activity.get_times()
            y: list[list[int]] = list()
            legend: list[str] = list(gender_times.keys())
            for time_values in gender_times.values():
                newY = list()
                for value in time_values.values():
                    newY.append(value)
                y.append(newY)

            table_data: TableData = TableData(x, y, activity_name, show_linear, legend)
            self.show_plot(table_data)

    def get_activity_names(self) -> list[str]:
        return list(self.activities.keys())
