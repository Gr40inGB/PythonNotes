import datetime
import itertools
from abc import ABC


class Note(ABC):
    __id_iter = itertools.count(1)
    __id: int
    __data: datetime
    __title: str
    __text: str

    def __init__(self, title, text, note_id=0, date=datetime.datetime.now()):
        self.__id = next(Note.__id_iter) if note_id == 0 else note_id
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
        return '№ ' + str(self.id) + ' << ' + self.title + ' >> ' + self.date + '\n' + self.text
