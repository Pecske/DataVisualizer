class Activity:
    def __init__(self,name) -> None:
        self.name : str = name
        self.activities : list[Activity] = []
        self.timeValueDict : dict[str,int] = {}

    def add_activity(self,activity) -> None:
        self.activities.append(activity)

    def add_subGroup(self,name : str,value : int) -> None:
        self.timeValueDict[name]=value