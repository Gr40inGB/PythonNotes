from CommunicationsAxes.view.console_view import ConsoleView
from dataBase.DataBaseImitation import JsonData
from model.NoteBook import Notebook


class Controller:

    def __init__(self, data: JsonData, n_book: Notebook, view: ConsoleView):
        self.__data = data
        self.__book = n_book
        self.__view = view
        self.__working = True
        self.menu_list = {
            1: ('create', self.create),
            2: ('delete', self.delete),
            3: ('edit', self.delete),
            4: ('show', self.delete),
            5: ('exit', self.delete),
        }

    def start(self):
        while self.__working:
            text = ''
            for k, v in self.menu_list.items():
                text = text + str(k) + ': ' + v[0] + '\n'
            to_run = self.menu_list.get(self.__view.input_num(text + 'please select >>>  ', len(self.menu_list)))
            to_run[1]()

    @property
    def data(self):
        return self.__data

    @property
    def book(self):
        return self.__book

    @property
    def view(self):
        return self.__view

    def save_new_data(self):
        self.__data.write_all(self.book.notes)

    def menu(self):
        menu_list = {1: self.create,
                     2: self.delete}

    def create(self):
        self.__book.create(self.__view.input_str('Please input title: '), self.__view.input_str('Please input text: '))
        self.save_new_data()

    def delete(self):
        print('delete')

    def select(self):
        pass

    def edit(self):
        pass
