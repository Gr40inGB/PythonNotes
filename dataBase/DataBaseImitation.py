import json
import os.path

from model.note import Note


class jsonData():
    def __init__(self, filename):

        self.filename = filename

    def read_all(self):
        all_notes = list()
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding='utf-8') as file:
                    data = json.loads(file.read())
                    data.sort(key=lambda x: x['date'])
                for item in data:
                    all_notes.append(Note(item['title'], item['text'], item['id'], item['date']))
                return all_notes
            except ValueError:
                print('Error')
                return all_notes

    def write_all(self, new_notes: list[Note]):
        to_json_string = list()
        for note in new_notes:
            to_json_string.append({'id': note.id, 'date': note.date, 'title': note.title, 'text': note.text})

        with open(self.filename, "w", encoding='utf-8') as my_file:
            my_file.write(json.dumps(to_json_string, indent=4, ensure_ascii=False, sort_keys=False, default=str))
