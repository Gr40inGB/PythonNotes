from CommunicationsAxes.view.console_view import ConsoleView
from controller.controller import Controller
from dataBase.DataBaseImitation import JsonData
from model.NoteBook import Notebook


def start():
    db = JsonData('base.json')
    app_controller = Controller(db, Notebook(db.read_all()), ConsoleView())

    app_controller.start()


if __name__ == '__main__':
    start()
