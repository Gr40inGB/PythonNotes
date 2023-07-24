from dataBase.DataBaseImitation import jsonData
from model.note import Note


def start():
    n = Note('BLA', 'blablalbla')
    n2 = Note('BLA', 'blablalbla')
    n3 = Note('BLA', 'blablalbla')
    # print(n)
    # print(n2)
    # print(n3)

    # print(n.date)
    notess = [n, n2, n3]
    db = jsonData('base.json')

    current_notes= db.read_all()
    for note in current_notes:
        print(note)

    # db.write_all(notess)


if __name__ == '__main__':
    start()
