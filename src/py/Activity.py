import collections
from GenderName import GenderName
from BaseData import BaseData


class Activity(BaseData):

    VALUE_LABEL = "Fő / Perc"

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.activities: list[Activity] = list()
        self.gender_time: dict[GenderName,dict[str,int]] = dict()
        self.times: list[str] = list()

    def add_activity(self, activity) -> None:
        self.activities.append(activity)

    def add_gender_time(self,gender : GenderName, time : str, value : int) -> None:
        if gender not in self.gender_time:
            self.gender_time[gender] = dict()
        self.gender_time[gender][time] = value
    
    def filter_time_values_by_gender(self, genders: list[GenderName] = None) -> dict[GenderName,dict[str,int]]:
        result : dict[GenderName,dict[str,int]] =dict()
        if genders is None or len(genders) == 0:
            return self.gender_time
        else:
            for k,v in self.gender_time.items():
                if k in genders:
                    result[k] = v
        return result

    def get_times(self) -> list[str]:
        times: dict[int, str] = dict()
        for time_value in self.gender_time.values():
            for k in time_value.keys():
                split_time: list[str] = k.split("/")
                if len(split_time) == 2:
                    time = int(split_time[0])
                    times[time] = k
        times = collections.OrderedDict(sorted(times.items()))
        return list(times.values())
