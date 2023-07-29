## Так
### Пытался писать как учили на java и получилось явно не питонисто, но работает


# Note
```python

class Note(ABC):
    __id_iter = itertools.count(1)
    __id_max = 0
    __id: int
    __data: datetime
    __title: str
    __text: str

    def __init__(self, title, text, note_id=0, date=datetime.datetime.now()):
        self.__id = next(Note.__id_iter) if note_id == 0 else note_id
        Note.__id_max = self.__id if Note.__id_max <= self.__id else Note.__id_max
        Note.__id_iter = itertools.count(Note.__id_max + 1)
        self.__date = date
        self.__title = title
        self.__text = text

    @property
    def iterator(self):
        return self.__id_iter

    @iterator.setter
    def iterator(self, new_iterator_max):
        self.__id_iter = new_iterator_max

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

```

# Notebook

```python

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

```
# JSON
```python

class JsonData:
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
                    all_notes.append(
                        Note(item['title'],
                             item['text'],
                             item['id'],
                             datetime.datetime.strptime(item['date'], '%d.%m.%Y %H:%M')))
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

```

# Controller 

```python

class Controller:

    def __init__(self, data: JsonData, n_book: Notebook, view: ConsoleView):
        self.__data = data
        self.__book = n_book
        self.__view = view
        self.__working = True
        self.menu_list = {
            1: ('show all', self.show_all),
            2: ('create', self.create),
            3: ('show', self.show),
            4: ('delete', self.delete),
            5: ('edit', self.edit),
            6: ('time interval', self.show_time_interval),
            7: ('exit', self.exit),
        }

    def start(self):
        while self.__working:
            text = ''
            for k, v in self.menu_list.items():
                text = text + str(k) + ': ' + v[0] + '   \t'
            to_run = self.menu_list.get(self.__view.input_num_max(text + '\nplease select >>>  ', len(self.menu_list)))
            to_run[1]()
            self.save_new_data()

    def exit(self):
        self.__view.show_info("buy buy =) ")
        self.__working = False

    @property
    def data(self):
        return self.__data

    @property
    def book(self):
        return self.__book

    @property
    def view(self):
        return self.__view

    def save_new_data(self):
        self.__data.write_all(self.book.notes)

    def create(self):
        self.__book.create(self.__view.input_str('Please input title: '), self.__view.input_str('Please input text: '))
        # self.save_new_data()

    def delete(self):
        self.__view.show_info('Now selected id will delete!')
        temp_link = self.select()
        if temp_link is not None:
            self.__book.delete(temp_link)
        else:
            self.__view.show_info('Not found that id :(')

    def select(self):
        self.__view.show_info(self.__book.only_title)
        temp_link = self.book.select(self.__view.input_num('please select id: '))
        return temp_link

    def show(self):
        temp_link = self.select()
        self.__view.show_info(temp_link) if temp_link is not None else self.__view.show_info('Not found that id!')

    def show_all(self):
        self.__view.show_info(self.book)

    def show_time_interval(self):
        time_start = datetime.datetime(year=self.__view.input_num_max('input start year: ', datetime.MAXYEAR),
                                       month=self.__view.input_num_max('input start month: ', 12),
                                       day=self.__view.input_num_max('input start day: ', 31),
                                       minute=0, second=0, microsecond=0)
        time_end = datetime.datetime(year=self.__view.input_num_max('input end year: ', datetime.MAXYEAR),
                                     month=self.__view.input_num_max('input end month: ', 12),
                                     day=self.__view.input_num_max('input end day: ', 31),
                                     minute=59, second=59, microsecond=999999)

        self.__view.show_info(self.book.show_time_interval(time_start, time_end))

    def edit(self):
        self.__view.show_info('Select id for edit: ')
        temp_link = self.select()
        self.__book.edit(temp_link, self.__view.input_str('Please input title: '),
                         self.__view.input_str('Please input text: '))

```