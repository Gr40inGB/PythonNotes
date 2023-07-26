from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self):
        self.working = True

    @staticmethod
    @abstractmethod
    def start(self):
        pass

    @staticmethod
    @abstractmethod
    def stop(self):
        self.working = False

    @staticmethod
    @abstractmethod
    def show_info(self, info: str):
        pass


def input_num(message: str) -> int:
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
            return temp


class ConsoleView(View):
    @staticmethod
    def stop(self):
        self.working = False

    @staticmethod
    def start(self):
        while self.working:
            self.run_command(self.show_menu())

    @staticmethod
    def show_info(self, **kwargs):
        pass
