from pandas import DataFrame
from Activity import Activity
from TableData import TableData
from GenderName import GenderName
from BaseDataService import BaseDataService
from ItemName import ItemName


class ActivityService(BaseDataService):
    def __init__(self, df: DataFrame) -> None:
        super().__init__(df)

    def _get_gender(self, s: str) -> GenderName:
        for name in GenderName:
            if name.value == s:
                return name

    def map_df_to_base_data(self, df):
        rotated_data_frame: dict[str, int] = df.set_index(df.columns[0]).T.to_dict(
            "list"
        )
        activities: dict[str, Activity] = dict()
        for k, v in rotated_data_frame.items():
            new_activity: Activity = Activity(k)
            column_index: int = 1
            for value in v:
                gender_time : str = df.columns[column_index]
                gender_time_split : list[str] = gender_time.split(" ")
                if len(gender_time_split) == 2:
                    gender_name : GenderName = self._get_gender(gender_time_split[0])
                    time : str = gender_time_split[1]
                    new_activity.add_gender_time(gender_name,time,int(value))                    
                #new_activity.add_time_value(str(df.columns[column_index]), int(value))
                column_index = column_index + 1
            if k not in activities:
                activities[k] = new_activity
            if k[0].isupper():
                current_parent = k
            if k[0].islower() and current_parent in activities:
                parent: Activity = activities.get(current_parent)
                parent.add_activity(new_activity)
        return activities

    def map_base_data_to_table(self, filters):
        activity_name: str = filters.get(ItemName.activity)
        if activity_name in self.base_data_map:
            current_activity: Activity = self.base_data_map.get(activity_name)
            gender_filters: list[str] = filters.get(ItemName.gender)
            genders: dict[GenderName, dict[str, int]] = (
                current_activity.filter_time_values_by_gender(gender_filters)
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
                filters.get(ItemName.linear),
            )
        return table_data

    def get_activity_names(self) -> list[str]:
        return list(self.base_data_map.keys())
