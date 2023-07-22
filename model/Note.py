import datetime
import itertools


class Note(object):
    __id_iter = itertools.count(1)
    __id: int
    __data: datetime
    __title: str
    __text: str

    def __init__(self, date, title, text):
        self.__id = next(Note.__id_iter)
        self.__date = date
        self.__title = title
        self.__text = text

    @property
    def id(self):
        return self.__id

    @property
    def date(self):
        return datetime.datetime.strftime(self.__date, '%d.%m.%Y %H:%M')

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    def __str__(self) -> str:
        return '№' + str(self.id) + ' << ' + self.title + ' >> ' + self.date + '\n' + self.text
