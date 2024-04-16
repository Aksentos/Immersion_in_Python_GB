"""Задание №1
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
# var 1
from string import ascii_letters
import unittest


def del_string(text: str):
    ans = ""
    for char in text:
        if char in ascii_letters or char == " ":
            ans += char
    return ans.lower()


print(del_string("dfgSDF fsdf12 !!! dfg"))

# var 2
def not_punctuation(texts):
    return "".join(text for text in texts if text in ascii_letters or text == " ")


# var 3
def del_chars(text)
    return ''.join(i.lower() for i in text if i.isalpha() or i.isspace()) #or unicodedata.name(i).startswith('LATIN'))

"""Задание №2
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
def not_punctuation(texts):
    """not_punctuation funk
    >>> not_punctuation('one two')
    'one two'
    >>> not_punctuation('ONE two')
    'one two'
    >>> not_punctuation('one! two?')
    'one two'
    >>> not_punctuation('one twцццo')
    'one two'
    >>> not_punctuation('ONE twцццo!!!')
    'one two'
    """

    return "".join(
        text for text in texts if text in ascii_letters or text == " "
    ).lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


"""Задание №3
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import unittest

class TestCaseName(unittest.TestCase):

    def test_nochanges(self):
        self.assertEqual('one two', not_punctuation('one two'))

    def test_up_low(self):
        self.assertEqual('one two', not_punctuation('ONE two'))

    def test_punctuation(self):
        self.assertNotEqual('one, two!', not_punctuation('one, two!'))

    def test_another_lang(self):
        self.assertEqual('one two', not_punctuation('one twoцццц'))

    def test_all_tests(self):
        self.assertEqual('one two', not_punctuation('ONE twцццo!!!'))


# if __name__ == '__main__':
#     unittest.main(verbosity=2)


'''Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов(кроме п. 1)
'''
import pytest

def test_no_changes():
    assert 'one two' == not_punctuation('one two')

def test_up_to_low():
    assert 'one two' == not_punctuation('ONE two')

def test_punctuation():
    assert 'one, two!' != not_punctuation('one, two!')

def test_another_lang():
    assert 'one two' == not_punctuation('one twoцццц')

def test_all_tests():
    assert 'one two' == not_punctuation('ONE twцццo!!!')


if __name__ == '__main__':
    pytest.main(['-v'])


"""Задание №5
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
import unittest

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        total_perimeter = self.perimeter() + other.perimeter()
        new_length = total_perimeter / 4
        return Rectangle(new_length, self.width)

    def __sub__(self, other):
        diff_perimeter = abs(self.perimeter() - other.perimeter())
        new_length = diff_perimeter / 2
        return Rectangle(new_length, self.width)

    def __eq__(self, value: object) -> bool:
        return self.length == value.length and self.width == value.width


class TestCheckRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(5, 3)
        self.rect2 = Rectangle(4, 4)
        self.rect3 = Rectangle(4, 2)

    def test_perimeter(self):
        self.assertEqual(self.rect1.perimeter(), self.rect2.perimeter())

    def test_area(self):
        self.assertEqual(self.rect1.area(), 15)
        self.assertEqual(self.rect2.area(), 16)

    def test_add(self):
        a = self.rect1 + self.rect2
        self.assertTrue(a == Rectangle(8, 3))

    def test_sub(self):
        b = self.rect1 - self.rect3
        self.assertTrue(b == Rectangle(2, 3))

if __name__ == '__main__':
    unittest.main(verbosity=2)


"""Задание №6
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""
class User:
    def __init__(self, name: str, u_id: str, u_lvl: int):
        self.name = name
        self.id = u_id
        self.lvl = u_lvl

    def __hash__(self):
        return hash(self.id + self.name)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.id == other.id and self.name == other.name

    def __repr__(self):
        return f"{self.name} (ID: {self.id}, Уровень доступа: {self.lvl})"
    
class MyAppException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f"Ошибка приложения! {self.msg}"


class MyAccessError(MyAppException):
    def __init__(self, name: str, u_id: str):
        super().__init__(
            f"Пользователя с таким именем ({name}) и ID({u_id}) не существует!"
        )


class MyLevelError(MyAppException):
    def __init__(self, my_level: int, new_level: int):
        super().__init__(
            f"Ошибка доступа! Уровень доступа нового пользователя ({new_level}) меньше вашего уровня ({my_level})"
        )


class MyIDError(MyAppException):
    def __init__(self, u_id: str):
        super().__init__(f"Пользователь с таким ID ({u_id}) уже существует!")


class MyLoginError(MyAppException):
    def __init__(self):
        super().__init__(f"Пользователь не залогирован!")


import json


class Company:
    _company = None
    _file_name = None

    def __new__(cls, name: str = None, db_file: str = "user_list.json"):
        if cls._company is None:
            cls._company = super().__new__(cls)
            cls._company.name = name
            cls._file_name = db_file
            cls._company._logged_in = None
        return cls._company

    def __init__(self, *args, **kwargs):
        self._logged_in: User | None = None

    @property
    def users_list(self):
        result = set()
        for lvl, user in self._load_json().items():
            for u_id, name in user.items():
                result.add(User(name, u_id, lvl))
        return result

    @classmethod
    def _load_json(cls):
        with open(cls._file_name, "r", encoding="UTF-8") as json_file:
            return json.load(json_file)

    @classmethod
    def _save_json(cls, data: dict):
        with open(cls._file_name, "w", encoding="UTF-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    def _add_new_user(self, new_user: User):
        users_data = self._load_json()
        if str(new_user.lvl) in users_data:
            users_data[str(new_user.lvl)][new_user.id] = new_user.name
        else:
            users_data[str(new_user.lvl)] = {new_user.id: new_user.name}
        self._save_json(users_data)

    def login(self, name: str, u_id: str):
        login_user = User(name, u_id, 0)
        if login_user in self.users_list:
            for user in self.users_list:
                if user == login_user:
                    # print(f'Здравствуйте, {user.name}!\nАвторизация прошла успешно! Ваш уровень доступа: {user.lvl}')
                    self._logged_in = user
                    return user.lvl
        raise MyAccessError(name, u_id)

    def logout(self):
        print(f"До свидания, {self._logged_in.name}! До новых встреч!")
        self._logged_in = None

    def new_user(self, user_name: str, u_id: str, new_lvl: int):
        if self._logged_in:
            if new_lvl < int(self._logged_in.lvl):
                raise MyLevelError(self._logged_in.lvl, new_lvl)
            new_user = User(user_name, u_id, new_lvl)
            if u_id in {user.id for user in self.users_list}:
                raise MyIDError(u_id)
            self._add_new_user(new_user)
        else:
            raise MyLoginError()


import pytest


@pytest.fixture()
def company():
    return Company("Adidas")


@pytest.fixture()
def user_sham():
    return "Шамиль", "23"


@pytest.fixture()
def new_user_17000():
    return "Василий", "17000", 5


@pytest.fixture()
def new_user_17():
    return "Василий", "17", 7


def test_login_error(company, new_user_17):
    with pytest.raises(MyAccessError):
        company.login(*new_user_17[:2])


def test_new_user_error(company, user_sham, new_user_17000):
    with pytest.raises(MyLevelError):
        company.login(*user_sham)
        company.new_user(*new_user_17000)


def test_id_error(company, user_sham, new_user_17):
    with pytest.raises(MyIDError):
        company.login(*user_sham)
        company.new_user(*new_user_17)


def test_login(company, user_sham):
    assert company.login(*user_sham) == "6"


if __name__ == "__main__":
    pytest.main(["-v"])
