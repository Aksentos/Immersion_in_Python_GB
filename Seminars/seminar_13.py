"""Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def num_input():
    while True:
        try:
            num = float(input("Введите целое или вещественное число: "))
            if num == int(num):
                return int(num)
            return num
        except ValueError:
            print("Введено не число! попробуйте еще раз")


print(num_input())


"""Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""
data_dict = {1: "one", 2: "two"}


def get_dict(dictionary: dict, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default


print(get_dict(data_dict, 1))  # one
print(get_dict(data_dict, 4))  # None
print(get_dict(data_dict, 5, default="Такого ключа нет"))  # Такого ключа нет


"""Задание №3
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class MyAppException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f"Ошибка приложения! {self.msg}"


class MyValueError(MyAppException):
    def __init__(self, value: int):
        super().__init__(f"Неверное значение: {value}")


class MyLevelError(MyAppException):
    def __init__(self, level: int):
        super().__init__(f"Ошибка доступа: {level}")


"""Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
import json
import os


class User:
    def __init__(self, name: str, u_id: str, u_lvl: int):
        self.name = name
        self.id = u_id
        self.lvl = u_lvl

    def __hash__(self):
        return hash(self.name + self.id)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.__hash__() == other.__hash__()

    def __repr__(self):
        return f"{self.name} (ID: {self.id}, Уровень доступа: {self.lvl})"


def input_name(message: str) -> str:
    return input(message)


def input_lvl(message: str, error_message: str, limits: tuple[int, int]) -> str:
    while True:
        level = input(message)
        if level.isdigit() and limits[0] <= int(level) <= limits[1]:
            return level
        print(error_message)


def input_id(
    message: str, error_message: str, id_is_exists: str, id_list: list[str]
) -> str:
    while True:
        user_id = input(message)
        if user_id.isdigit():
            if user_id not in id_list:
                return user_id
            else:
                print(id_is_exists)
        else:
            print(error_message)


def input_users(file_name: str) -> None:
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            users_dict = json.load(file)
    else:
        users_dict = {}
    users_id_list = [u_id for users in users_dict.values() for u_id in users]
    while True:
        user_name = input_name("Введите имя пользователя: ")
        if not user_name:
            break
        user_id = input_id(
            "Введите ID пользователя: ",
            "ID должен состоять исключительно из цифр!",
            "Пользователь с таким ID уже существует!",
            users_id_list,
        )
        user_level = input_lvl(
            "Введите уровень доступа пользователя от 1 до 7: ",
            "Нужно ввести число от 1 до 7!",
            (1, 7),
        )
        # users_levels_list = sorted(users_dict, key=lambda x: int(x))
        # users_dict = {user_lvl: users_dict[user_lvl] for user_lvl in users_levels_list}
        if user_level in users_dict:
            users_dict[user_level][user_id] = user_name
        else:
            users_dict[user_level] = {user_id: user_name}
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(users_dict, file, indent=4, ensure_ascii=False, sort_keys=True)
        users_id_list.append(user_id)


def make_user_from_json(file_name: str):
    result = set()
    with open(file_name, "r", encoding="UTF-8") as json_file:
        users_data = json.load(json_file)
    for lvl, user in users_data.items():
        for u_id, name in user.items():
            result.add(User(name, u_id, lvl))
    return result


input_users("user_list.json")
print(make_user_from_json("user_list.json"))


"""Задание №5 + Задание №6
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
import json

from main import User

# from app_exception import *  # На семинаре был создан отдельный файл с обработкой исключений


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
                    print(
                        f"Здравствуйте, {user.name}!\nАвторизация прошла успешно! Ваш уровень доступа: {user.lvl}"
                    )
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
            if new_user in self.users_list:
                raise MyIDError(u_id)
            self._add_new_user(new_user)
        else:
            raise MyLoginError()


if __name__ == "__main__":
    a = Company("GB")
    a.login("Максим", "45")
    a.new_user("Ирина", "727", 3)
    a.logout()
    a.new_user("Катя", "234", 6)


"""Классы обработки исключений для задачи 5/6"""

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
