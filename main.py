import datetime

from model.Note import Note


def start():
    n = Note(datetime.datetime.now(), 'BLA', 'blablalbla')
    n2 = Note(datetime.datetime.now(), 'BLA', 'blablalbla')
    n3 = Note(datetime.datetime.now(), 'BLA', 'blablalbla')
    print(n)
    print(n2)
    print(n3)


if __name__ == '__main__':
    start()

