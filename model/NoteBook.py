from CommunicationsAxes.Axes import Axes
from model.note import Note


class Notebook(Axes):

    def __init__(self, notes_list: list[Note]):
        self.__notes_list = notes_list

    @property
    def notes(self):
        return self.__notes_list

    @notes.setter
    def notes(self, new_notes_list):
        self.__notes_list = new_notes_list

    def create(self, title, text):
        self.__notes_list.append(Note(title, text))

    def read(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass
