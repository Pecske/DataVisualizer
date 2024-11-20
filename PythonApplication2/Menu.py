from collections.abc import Callable
from ActivityService import ActivityService


class Menu:
    
    def __init__(self,activity_service : ActivityService) -> None:
        self.activity_service = activity_service
        self.filter_method : dict[str,Callable] = {1:self.activity_service.show_activity, 2:self.activity_service.show_activity_plot_by_gender}

    def __print_options(self,options : dict[int,str]) -> None:
        print("-------------------------")
        for k,v in options.items():
            print("[{0}]: {1}".format(k,v))
        print("-------------------------")

    def __create_options_from_names(self,optionNames: list[str]) -> dict[int,str]:
        options : dict[int,str] = dict()
        index : int = 1
        for optionName in optionNames:
            options[index] = optionName
            index += 1
        return options

    def __get_input_value(self,options: dict[int,str]) -> str:
        option_key : str = self.__get_input_key(options)
        return options.get(option_key)

    def __get_input_key(self,options: dict[int,str]) -> int:
        validInput : bool = False        
        while(validInput == False):
            try:
                current_option : int = int(input("Input: "))
                if(current_option in options.keys()):
                    validInput = True
                else:
                    print("Input is out of bounds")
            except:
                print("Invalid input\n")
                validInput = False
        return current_option

    def __convert_yes_no_to_bool(self,s : str) -> bool:
        s = s.lower()
        conversion_dict : dict[str,bool] = {"y":True,"n":False}
        return conversion_dict.get(s[0])

    def get_chosen_category(self, optionNames : list[str]) -> str:
        options : dict [int,str] = self.__create_options_from_names(optionNames)
        print("Choose an activity to be shown (press the number associated with it):")
        self.__print_options(options)
        return self.__get_input_value(options)

    def is_linear_regression_shown(self) -> bool:
        options : dict[int,str] = {1:"Yes",2:"No"}
        print("Do u want linear regression to be shown?")
        self.__print_options(options)
        isLinear : str = self.__get_input_value(options)
        return self.__convert_yes_no_to_bool(isLinear)

    def choose_filter(self) -> int:
        options : dict[int,str] = {1:"All", 2:"By Gender"}
        print("Apply a filter: ")
        self.__print_options(options)
        return self.__get_input_key(options)

    def run_visualization_loop(self) -> None:
        while True:
            print("\033[H\033[3J", end="") # ANSI escape code to clear console
            chosen_category = self.get_chosen_category(self.activity_service.get_activity_names())
            show_linear = self.is_linear_regression_shown()
            activity_filter: int = self.choose_filter()
            self.filter_method.get(activity_filter)(chosen_category,show_linear)

            # Check if the user wants to continue
            options: dict[int, str] = {1: "Yes", 2: "No"}
            print("Would you like to visualize another data point?")
            self.__print_options(options)

            continue_choice = self.__get_input_value(options)

            if continue_choice == "No":
                print("Exiting program. Goodbye!")
                break
