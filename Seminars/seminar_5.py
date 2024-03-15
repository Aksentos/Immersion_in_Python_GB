"""Задание №1
Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""

s = "1/33/4/234/111"
v1, k1, k2, *v2 = map(int, s.split("/"))
print(ans := {k1: v1, k2: v2})


"""Задание №2
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

print({i: ord(i) for i in input("Введите любой текст: ")})


"""Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
# var 1
text = {"ы": 1099, "в": 1074, "а": 1072, "п": 1087}
ans = iter(text.items())
for _ in range(5):
    print(next(ans, "пар больше нет"))

# var 2
print(dictionary := {i: ord(i) for i in "Самостоятельно сохраните "})
a = iter(dictionary.items())
print(*(next(a) for _ in range(5)))


"""Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

# var 1
print(
    list(num for num in range(0, 101, 2) if sum(int(digit) for digit in str(num)) != 8)
)

# var 2

gen_even = (i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8)
print(*gen_even)

# var 3
gen_even = (i for i in range(0, 101, 2) if (i // 10 + i % 10) != 8)
print(*gen_even)


"""Задание №5
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
"""

# var 1
answer = []
for num in range(100):
    if not num % 15:
        num = "FizzBuzz"
    elif not num % 5:
        num = "Buzz"
    elif not num % 3:
        num = "Fizz"
    answer.append(num)

# var 2
res = (
    "fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
    for i in range(1, 101)
)
print(*res)


# var 3
def num_print_friz_buzz(num):
    for n in range(1, num + 1):
        if not n % 3 and not n % 5:
            yield "FizzBuzz"
        elif not n % 3:
            yield "Fizz"
        elif not n % 5:
            yield "Buzz"
        else:
            yield n


for i in num_print_friz_buzz(100):
    print(i)


"""Задание №6
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку.
"""
# var 1
for i in (0, 4):
    print("\t")
    for k in range(1, 11):
        print("\t")
        for j in range(2 + i, 6 + i):
            print(f"{j:^3} * {k:^3} = {k * j:^3}", end="\t")

# var 2
print(
    "\n\n".join(
        [
            "\n".join(
                [
                    "\t".join([f"{x:^3}x{y:^3}= {x*y:^3}" for x in range(2 + k, 6 + k)])
                    for y in range(2, 11)
                ]
            )
            for k in (0, 4)
        ]
    )
)


"""Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


# var 1
def generat_pr(number):
    num = 2
    count = 0
    while count < number:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num
            count += 1
        num += 1


for i in generat_pr(20):
    print(i, end=" ")


# var 2 бесконечный цикл
def func_gen():
    number = 0
    while True:
        number += 1
        if number in (1, 2, 3):
            yield number
            continue
        if not number % 2:
            continue
        for dev in range(3, int(number**0.5) + 1, 2):
            if not number % dev:
                break
        else:
            yield number


gen = func_gen()

for _ in range(10):
    print(next(gen))


# var 3
def generate_numbers():
    for n in range(2, N):
        if is_number(n):
            yield n


def is_number(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True


primes = generate_numbers()
for _ in range(N):
    print(next(primes))
