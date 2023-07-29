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
            1: ('show all', self.show_all),
            2: ('create', self.create),
            3: ('show', self.show),
            4: ('delete', self.delete),
            5: ('edit', self.edit),
            6: ('exit', self.delete),
        }

    def start(self):
        while self.__working:
            text = ''
            for k, v in self.menu_list.items():
                text = text + str(k) + ': ' + v[0] + '   \t'
            to_run = self.menu_list.get(self.__view.input_num_max(text + '\nplease select >>>  ', len(self.menu_list)))
            to_run[1]()
            self.save_new_data()

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

    def create(self):
        self.__book.create(self.__view.input_str('Please input title: '), self.__view.input_str('Please input text: '))
        # self.save_new_data()

    def delete(self):
        self.__view.show_info('Now selected id will delete!')
        temp_link = self.select()
        if temp_link is not None:
            self.__book.delete(temp_link)
        else:
            self.__view.show_info('Not found that id :(')

    def select(self):
        self.__view.show_info(self.__book.only_title)
        temp_link = self.__book.select(self.__view.input_num('please select id: '))
        return temp_link

    def show(self):
        temp_link = self.select()
        self.__view.show_info(temp_link) if temp_link is not None else self.__view.show_info('Not found that id!')

    def show_all(self):
        self.__view.show_info(self.__book)

    def edit(self):
        self.__view.show_info('Select id for edit: ')
        temp_link = self.select()
        self.__book.edit(temp_link, self.__view.input_str('Please input title: '),
                         self.__view.input_str('Please input text: '))
