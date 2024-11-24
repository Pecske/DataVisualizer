import collections
from GenderName import GenderName


class Activity:

    VALUE_LABEL = "Fő / Perc"

    def __init__(self, name) -> None:
        self.name: str = name
        self.activities: list[Activity] = list()
        self.time_values: dict[str, int] = dict()

    def _get_gender(self, s: str) -> GenderName:
        for name in GenderName:
            if name.value == s:
                return name

    def _map_gender_time_to_dict(
        self,
        gender: GenderName,
        time: str,
        v: int,
        result: dict[GenderName, dict[str, int]],
    ):
        if gender not in result:
            result[gender] = {time: v}
        else:
            result[gender][time] = v

    def add_activity(self, activity) -> None:
        self.activities.append(activity)

    def add_time_value(self, name: str, value: int) -> None:
        self.time_values[name] = value

    def get_value_by_gender(
        self, genders: list[GenderName] = None
    ) -> dict[GenderName, dict[str, int]]:
        result: dict[GenderName, dict[str, int]] = dict()
        for k, v in self.time_values.items():
            split_line: list[str] = k.split(" ")
            if len(split_line) == 2:
                gender: GenderName = self._get_gender(split_line[0])
                time: str = split_line[1]
                if genders is not None and len(genders) > 0:
                    if gender in genders:
                        self._map_gender_time_to_dict(gender, time, v, result)
                else:
                    self._map_gender_time_to_dict(gender, time, v, result)

        return result

    def get_times(self) -> list[str]:
        times: dict[int, str] = dict()
        for k, v in self.time_values.items():
            split_group: list[str] = k.split(" ")
            if len(split_group) == 2:
                gender: str = split_group[0]
                time: str = split_group[1]
                time_split: list[str] = time.split("/")
                key = int(time_split[0])
                times[key] = time
        times = collections.OrderedDict(sorted(times.items()))
        return list(times.values())
