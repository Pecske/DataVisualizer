import collections


class Activity:
    def __init__(self,name) -> None:
        self.name : str = name
        self.activities : list[Activity] = list()
        self.time_values : dict[str,int] = dict()

    def add_activity(self,activity) -> None:
        self.activities.append(activity)

    def add_sub_group(self,name : str,value : int) -> None:
        self.time_values[name]=value

    def get_group_by_gender(self) -> dict[str,dict[str,int]]:
        gender_time_dict : dict[str,dict[str,int]] = dict()
        for k,v in self.time_values.items():
           split_group : list[str] = k.split(" ")
           if(len(split_group) == 2):
                gender : str = split_group[0]
                time : str = split_group[1]
                if(gender not in gender_time_dict):
                    gender_time_dict[gender] = {time:v}
                else:
                    gender_time_dict[gender][time] = v
        return gender_time_dict

    def get_times(self) -> list[str]:
        times : dict [int,str] = dict()
        for k,v in self.time_values.items():
           split_group : list[str] = k.split(" ")
           if(len(split_group) == 2):
                gender : str = split_group[0]
                time : str = split_group[1]
                time_split : list[str] = time.split("/")
                key = int(time_split[0])
                times[key] = time
        times = collections.OrderedDict(sorted(times.items()))   
        return list(times.values())