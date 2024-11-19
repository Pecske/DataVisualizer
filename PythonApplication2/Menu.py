class Menu:
    
    def __print_options(self,options : dict[int,str]) -> None:
        print("-------------------------")
        for k,v in options.items():
            print("[{0}]: {1}".format(k,v))
        print("-------------------------")

    def __create_options_from_names(self,optionNames: list[str]) -> dict[int,str]:
        options : dict[int,str] = {}
        index : int = 1
        for optionName in optionNames:
            options[index] = optionName
            index += 1
        return options

    def __get_input_value(self,activityNames: dict[int,str]) -> str:
        options : dict[int,str] = {}
        validInput : bool = False        
        while(validInput == False):
            try:
                currentOption : int = int(input("Input: "))
                if(currentOption in activityNames.keys()):
                    validInput = True
                else:
                    print("Input is out of bounds")
            except:
                print("Invalid input\n")
                validInput = False
        return activityNames.get(currentOption)

    def __convert_yes_no_to_bool(self,s : str) -> bool:
        s = s.lower()
        conversionDict : dict[str,bool] = {"y":True,"n":False}
        return conversionDict[s[0]]

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

    def run_visualization_loop(self, activityService) -> None:
        while True:
           
            print("\033[H\033[3J", end="") # ANSI escape code to clear console

            chosen_category = self.get_chosen_category(activityService.get_activity_names())
            show_linear = self.is_linear_regression_shown()
            activityService.showPlot(chosen_category, show_linear)

            # Check if the user wants to continue
            options: dict[int, str] = {1: "Yes", 2: "No"}
            print("Would you like to visualize another data point?")
            self.__print_options(options)

            continue_choice = self.__get_input_value(options)

            if continue_choice == "No":
                print("Exiting program. Goodbye!")
                break
