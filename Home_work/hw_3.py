'''Список вещей для похода
На вход подается словарь со списком вещей для похода в качестве ключа и
их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную
грузоподъёмность.
Предметы не должны дублироваться.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и
сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную
backpack. Не выводите backpack на экран.
'''
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

# var 1
weight = 0
backpack = {}
for k, v in items.items():
    if v <= max_weight:
        weight += v
        if weight <= max_weight:
            backpack[k] = v

# var 2 (GB)
backpack = {}
for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight


"""Часто встречающиеся слова
В большой текстовой строке text подсчитать количество встречаемых слов и 
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд 
(после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов. Слова 
выведите в обратном алфавитном порядке.
"""
text = "Hello world. Hello Python.world Hello again. don`t 11 w w w".lower()
# var 1
import string

result = {}

# string.punctuation - все пунктуационные знаки (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
for i in string.punctuation: 
    text = text.replace(i, " ")  # заменяем пунктуационные знаки на пробелы
text = text.split() # делаем список всех слов

for item in set(text):
    if item.isalpha():  # проверка item состоит только из букв
        result[item] = text.count(item)

# сначала сортируем по ключу, затем по значению
answer = sorted(
    sorted(result.items(), key=lambda x: x[0], reverse=True),
    key=lambda x: x[1],
    reverse=True,
)
# Получаем 10 самых часто встречающихся слов
print(answer[:10])

# var 2 (GB)
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)

'''Cписок повторяющихся элементов
Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
'''
lst = [1, 1, 1, 1, 1]

# var 1
print(list(set([i for i in lst if lst.count(i) > 1])))

# var 2 (GB)
duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)
