from CommunicationsAxes.view.console_view import ConsoleView
from dataBase.DataBaseImitation import JsonData
from model.NoteBook import Notebook


class Controller:

    def __init__(self, data: JsonData, n_book: Notebook, view: ConsoleView):
        self.__data = data
        self.__book = n_book
        self.__view = view

    def menu(self):
        menu_list = {1: self.create,
                     2: self.create}

    def create(self):
        self.__book.create(input('Please input title: '), input('Please input text: '))


