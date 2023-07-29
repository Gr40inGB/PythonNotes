import datetime

from CommunicationsAxes.view.console_view import ConsoleView
from controller.controller import Controller
from dataBase.DataBaseImitation import JsonData
from model.NoteBook import Notebook


def start():
    db = JsonData('base.json')
    app_controller = Controller(db, Notebook(db.read_all()), ConsoleView())

    app_controller.start()
    # x = datetime.datetime.now()
    # time_start = datetime.datetime.strptime(
    #     input('input day: ') + '.' + input('input month: ') + "." + input('input year: ') + ' 00:00', '%d.%m.%Y %H:%M')
    # print(x)
    # print(time_start)
    # print(x < time_start)


if __name__ == '__main__':
    start()
