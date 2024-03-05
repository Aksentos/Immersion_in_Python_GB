'''Задача № 1
✔ Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
'''

from random import randint as ri

print(my_list := [ri(1,10) for _ in range(15)])

# var 1
print(list(set(my_list)))

# var 2
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# var 3
[new_list.append(item) for item in my_list if item not in new_list]
print(new_list)

'''Задача № 3
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.'''

my_tuple = (1, 'word', 'second', 3.14, (123, 'WTF?'), 33, True)

# var 1
my_dict = {}
for item in my_tuple:
    if type(item) not in my_dict:
        my_dict.setdefault(type(item), [item])
    else:
        my_dict[type(item)].append(item)

print(my_dict)

# var 2
result = {}

for item in my_tuple:
    if type(item) in result:
        result[type(item)].append(item)
    else:
        result[type(item)] = [item]

print(result)

"""Задача № 4
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""
from random import randint as ri

print(my_list := [ri(1, 5) for _ in range(10)])

# var 1
for i in my_list:
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)

print(my_list)

# var 2
print(new_list := [i for i in my_list if my_list.count(i) != 2])

"""' Задача № 5
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""
from random import randint as ri

print(my_list := [ri(1, 10) for _ in range(10)])
# var 1
print(*[i for i, value in enumerate(my_list, 1) if value % 2])

# var 2
[print(i, end=', ') for i, value in enumerate(my_list, 1) if value % 2]

# var 3
for i, value in enumerate(my_list, 1):
    if value % 2:
        print(i, end=' ')

"""Задача № 6
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""
# var 1
my_words = input("Введите строку текста: ").split()
max_word = max(len(item) for item in my_words)
my_words.sort()
for i, item in enumerate(my_words, 1):
    print(f"{i}{item:>{max_word + 1}}")

# var 2
max_len = len(max(my_words, key=len))
for i, item in enumerate(sorted(my_words), 1):
    print(f'{i}. {item:>{max_len}}')


"""Задание №7
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

text = "sdfg htyh dfgs trrhh"

# var 1
my_dict = {}
for symbol in set(text):
    my_dict[symbol] = text.count(symbol)
print(my_dict)

# var 2
my_dict = {}
for i in text:
    my_dict.setdefault(i, 0)
    my_dict[i] += 1
print(my_dict)

# var 3
my_dict = {}
for item in text:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict)


"""Задание №8
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
## var 1
friends = {
    "Ivan": ("matches", "food", "games", "umbrella"),
    "Bob": ("food", "games", "tent"),
    "Jack": ("food", "tent",  "phone"),
    # "Tom": ("tent", "shovel"),
}

# task 1 Какие вещи взяли все три друга
things = set()
for i in friends.values():
    things.update(set(i))  # наполняем множество уникальных наименований
print('В поход взяли:', *things)

# task 2 Какие вещи уникальны, есть только у одного друга
diff_things = []  # список для уникальных вещей
things = []  # список для перебора всех вещей
for value in friends.values():
    for i in value:
        if i not in diff_things:
            diff_things.append(i)  # добавляем вещь в уникальный список
        if i in things:
            diff_things.remove(i)  # если такая вещь есть в общем списке, удаляем её
        if i not in things:
            things.append(i)  # наполняем список всех вещей
print('Вещи которые взял кто-то один:', *diff_things)  # выводим список уникальных вещей

# task 3 Какие вещи есть у всех друзей кроме одного и имя того,
# у кого данная вещь отсутствует
all_things = []  # список для всех вещей и сколько их взяли
things = set()  # множество уникальных наименований как в task 1
for i in friends.values():
    things.update(set(i))  # наполняем множество уникальных наименований

for value in friends.values():
    for i in value:
        all_things.append(i)  # наполняем список для всех вещей и сколько их взяли

for k, v in friends.items():
    for i in things:
        if (  # проверка, если вещь взяли все кроме одного
            all_things.count(i) == len(friends) - 1
        ):
            if i not in v:
                print(f"{k} не взял {i}")  # выводим кто не взял вещь

## var 2
max_things = {
    "maksim": ("Телефон", "Бритва", "Галстук", "Шорты", "Рубашка"),
    "sergey": ("Телефон", "Шорты", "Зонтик", "Ключи", "Бритва"),
    "shamil": ("Телефон", "Бритва", "Рубашка", "Шорты", "Галстук"),
}

# 1 что взяли общего
all_things = set()
spisok = []
for value in max_things.values():
    all_things.update(set(value))
    for i in value:
        spisok.append(i)


# 2 Какие вещи уникальны, есть только у одного друга
one_thing = {}
for item in all_things:
    one_thing[item] = spisok.count(item)

for k, v in one_thing.items():
    if v == 1:
        print(f"{k}")

# 3 Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
dict_len = len(max_things)
for k, v in one_thing.items():
    if v == dict_len - 1:
        for name, values in max_things.items():
            if k not in values:
                print(f"{name} не взял {k}")

## var 3 (от Stone)
friends = {
    "Максим": ("топор", "вода", "еда", "палатка"),
    "Шамиль": ("топор", "вода", "закуска", "карты"),
    "Сергей": ("топор", "водка", "еда", "карты"),
}


all_things = set()
for friend_item in friends.values():
    all_things.update(set(friend_item))

have_all_friends = all_things.copy()
for friend_item in friends.values():
    have_all_friends.intersection_update(friend_item)
print("Вещи, которые есть у всех:")
print(*have_all_friends)
print()

only_one_friend = {}
for friend in friends:
    friend_backpack = set(friends[friend])
    for other_friend in friends:
        if friend != other_friend:
            friend_backpack.difference_update(friends[other_friend])
    if friend_backpack:
        only_one_friend[friend] = friend_backpack
print(
    "Есть только у одного:",
    *[f'{name}: {", ".join(back)}' for name, back in only_one_friend.items()],
    sep="\n",
)
print()

all_except_one_friend = {}
for friend in friends:
    friend_backpack = friends[friend]
    friends_backpacks = all_things.copy()
    for other_friend in friends:
        if friend != other_friend:
            friends_backpacks.intersection_update(friends[other_friend])
    friends_backpacks.difference_update(friend_backpack)
    if friends_backpacks:
        all_except_one_friend[friend] = friends_backpacks
print(
    "Есть у всех, кроме одного:",
    *[
        f'{name} не взял: {", ".join(back)}'
        for name, back in all_except_one_friend.items()
    ],
    sep="\n",
)
