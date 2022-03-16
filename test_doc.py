import unittest

documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
             {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

directories = {'1': ['2207 876234', '11-2'],
               '2': ['10006'],
               '3': []}

flag = False

def find_people(number):
    for document in documents:
        if document["number"] == number:
            return f'Документ с номером {document["number"]} принадлежит {document["name"]}'
    return f'Нет такого номера документа'

def find_shelf(number):
    keys = directories.keys()
    values = directories.values()
    zn = []
    for value in values:
        for val in value:
            zn.append(val)
    if number not in zn:
        return f"Вы ввели несуществующий номер документа"
    else:
        for key in keys:
            l = directories.get(key)
            if number in l:
                return f"Ключ находится на {key} полке"

def find_list(): # переделать для вывода всех
    for document in documents:
        print(document["type"],document["number"],document["name"])

def move(number, to_shelf):
    keys = directories.keys()
    values = directories.values()
    zn = []
    for value in values:
        for val in value:
            zn.append(val)
    if number not in zn:
        return "Вы ввели несуществующий номер документа"
    else:
        if to_shelf not in keys:
            return "Полки с данным номером ещё не создано, создайте вначале полку"
        else:
            for key in keys:
                l = directories.get(key)
                if number in l:
                    shelf = key
            counts2 = directories.get(shelf)
            counts2.remove(number)
            counts = directories.get(to_shelf)
            counts.append(number)

def add_shelf(number):
    if number in directories.keys():
        return "Полка с данным номером уже имеется"
    else:
        directories[number] = []

def add(number, type_d, name, shelf):
    keys = directories.keys()
    if shelf not in keys:
        return "Полки с данным номером ещё не создано, создайте вначале полку"
    else:
        value = {"type": type_d, "number": number, "name": name}
        documents.append(value)
        counts = directories.get(shelf)
        counts.append(number)
        return "Документ добавлен"

def delete(number):
    values = directories.values()
    keys = directories.keys()
    zn = []
    for value in values:
        for val in value:
            zn.append(val)
    if number not in zn:
        return "Вы ввели несуществующий номер документа"
    else:
        for document in documents:
            if document["number"] == number:
                type_d = document["type"]
                name = document["name"]
        for key in keys:
            l = directories.get(key)
            if number in l:
                shelf = key
        value = {"type": type_d, "number": number, "name": name}
        documents.remove(value)
        counts = directories.get(shelf)
        counts.remove(number)
        return "Документ удален"


class TestFunctions(unittest.TestCase):
    def setUp(self):
        print('setUp work')

    def tearDown(self):
        print('tearDown work')

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass - work')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass - work')


    def test_find_people(self):
        self.assertEqual(find_people('2207 876234'), 'Документ с номером 2207 876234 принадлежит Василий Гупкин')

    def test_add(self):
        self.assertEqual(add('12345', 'passport', 'Петя Скамейкин', '2'), 'Документ добавлен')

    def test_delete(self):
        self.assertTrue(delete('10006'))

unittest.main()
