from abc import ABC, abstractmethod

from model.note import Note


# CRUD
class Axes(ABC):
    @abstractmethod
    def create(self, title: str, text: str):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def edit(self, note: Note, title: str, text: str):
        pass

    @abstractmethod
    def delete(self, note: Note):
        pass
