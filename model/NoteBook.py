import datetime

from CommunicationsAxes.Axes import Axes
from model.note import Note


class Notebook(Axes):

    def __init__(self, notes_list: list[Note]):
        self.__notes_list = notes_list

    @property
    def notes(self):
        return self.__notes_list

    @property
    def size(self):
        return len(self.__notes_list)

    @property
    def only_title(self) -> str:
        titles = ''
        for note in self.notes:
            titles += str(note.id) + ' ' + note.title + '\t'
        return titles

    @notes.setter
    def notes(self, new_notes_list):
        self.__notes_list = new_notes_list

    def create(self, title, text):
        self.__notes_list.append(Note(title, text))

    def read(self):
        pass

    def edit(self, note, title, text):
        note.title = title
        note.text = text

    def delete(self, note):
        self.notes.remove(note)

    def select(self, searched_id):
        for note in self.notes:
            if note.id == searched_id:
                return note
        return None

    def __str__(self) -> str:
        text = ''
        for note in self.notes:
            text += str(note) + '\n\n'
        return text

    def show_time_interval(self, start: datetime, end: datetime):
        text = ''
        for note in self.notes:
            if start <= datetime.datetime.strptime(note.date, '%d.%m.%Y %H:%M') <= end:
                text += str(note) + '\n\n'
        return text
