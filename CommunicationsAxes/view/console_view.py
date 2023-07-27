from abc import ABC, abstractmethod


class View(ABC):
    @staticmethod
    @abstractmethod
    def show_info(self, info: str):
        pass

    @staticmethod
    @abstractmethod
    def input_num(message: str, max_value: int) -> int:
        pass

    @staticmethod
    @abstractmethod
    def input_str(message: str) -> str:
        pass


class ConsoleView(View):
    @staticmethod
    def show_info(self, info: str):
        print(info)

    @staticmethod
    def input_str(message: str) -> str:
        return input(message)

    @staticmethod
    def input_num(message: str, max_value: int) -> int:
        input_error: bool = True
        temp = -1
        while input_error:
            try:
                temp = int(input(message))
            except ValueError:
                print("You didn't enter a number!")
            else:
                if temp > max_value:
                    print("Number must be between 1 and " + str(max_value))
                else:
                    input_error = False

        return temp
