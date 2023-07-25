from abc import ABC, abstractmethod


# CRUD
class Axes(ABC):
    @abstractmethod
    def create(self, title: str, text: str):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def delete(self):
        pass
