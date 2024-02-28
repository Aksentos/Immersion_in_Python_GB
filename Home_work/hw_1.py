""" Задача № 1 Треугольник.
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
сообщить является ли треугольник разносторонним, равнобедренным или равносторонним,
только если треугольник существует .
"""

a, b, c = (
    int(input("Введите 1ю сторону: ")),
    int(input("Введите 2ю сторону: ")),
    int(input("Введите 3ю сторону: ")),
)  # это в автотест передавать не надо!
if a < b + c and b < a + c and c < a + b:
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")


""" Задача № 2 Простое или составное.
Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если это число натуральное и делится
нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается
отрицательное число или число более ста тысяч, выведите на экран сообщение: "Число должно быть
больше 1 и меньше 100000".
Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.
"""

num = int(input("Введите число: "))  # эту строчку в автотест передавать не надо!

# 1 варинат через функцию
def is_simple(number: int) -> str:
    if 1 < number < 100_001:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return "Не является простым"
        return "Простое"
    return "Число должно быть больше 1 и меньше 100000"

print(is_simple(num))


# 2 вариант без функции
if not 1 < num <= 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Не является простым")
            break
    else:
        print("Простое")


""" Задача № 3 Лотерея.
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
Числа в каждом списке не повторяются.
"""
# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# 1 вариант через множества
print("Количество совпадающих чисел:", len(set(list1).intersection(set(list2))))

# 2 вариант через цикл for и счетчик
counter = 0
for i in list1:
    if i in list2:
        counter += 1
print("Количество совпадающих чисел:", counter)
