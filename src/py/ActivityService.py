from pandas import DataFrame
from Activity import Activity
import matplotlib.pyplot as plt
import numpy as np
from TableData import TableData
from GenderName import GenderName


class ActivityService:
    def __init__(self, df: DataFrame) -> None:
        self.activities: dict[str, Activity] = self.convert_dataframe_to_activities(df)

    def __get_linear_regression_values(
        self, xValues: list[int], yValues: list[int]
    ) -> np.poly1d:
        coef = np.polyfit(xValues, yValues, 1)
        return np.poly1d(coef)

    def __map_columns_to_dummy_values(self, column_names: list[str]) -> list[int]:
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
                new_activity.add_time_value(str(df.columns[column_index]), int(value))
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
        plt.ylabel(table_data.value_label)
        plt.style.use("fivethirtyeight")
        for label, yValues in table_data.value_data.items():
            plt.plot(table_data.x, yValues, label=label)
            if table_data.isLinear:
                dummyX: list[int] = self.__map_columns_to_dummy_values(table_data.x)
                poly: np.poly1d = self.__get_linear_regression_values(dummyX, yValues)
                plt.plot(dummyX, poly(dummyX))

        plt.legend()
        plt.show()

    def create_table_data(
        self, activity_name: str, show_linear: bool, gender_filters: list[GenderName]
    ) -> TableData:
        if activity_name in self.activities:
            current_activity: Activity = self.activities.get(activity_name)
            genders: dict[GenderName, dict[str, int]] = (
                current_activity.get_value_by_gender(gender_filters)
            )
            x: list[str] = current_activity.get_times()
            value_data: dict[list[int], str] = dict()
            for k, v in genders.items():
                y: list[int] = list()
                for value in v.values():
                    y.append(value)
                if k.value not in value_data:
                    value_data[k.value] = y
            table_data: TableData = TableData(
                x,
                value_data,
                activity_name,
                current_activity.VALUE_LABEL,
                show_linear,
            )
        return table_data

    def get_activity_names(self) -> list[str]:
        return list(self.activities.keys())
