"""Работа с данными студентов"""

import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        self.is_valid_name(value)
        setattr(instance, self.param_name, value)

    def is_valid_name(self, value: str):
        if not ("".join(value.split()).isalpha() and value.istitle()):
            raise ValueError(
                "ФИО должно состоять только из букв и начинаться с заглавной буквы"
            )


class Student:
    name = NameValidator()

    def __init__(self, name, subjects) -> None:
        self.name = name
        self.subjects = self.load_subjects(subjects)

    @staticmethod
    def load_subjects(subjects_file: str):
        with open(subjects_file, "r", newline="", encoding="utf-8") as file:
            csv_file = csv.reader(file)
            for line in csv_file:
                subjects_dict = {
                    line[i]: {"grade": None, "test_score": None}
                    for i in range(len(line))
                }
        return subjects_dict

    @staticmethod
    def __is_valid_num(value):
        if not isinstance(value, int):
            raise TypeError(f"Значение {value} должно быть целым числом")

    @staticmethod
    def __is_valid_grade(value, min_number=2, max_number=5):
        text_error = f"Оценка должна быть целым числом от {min_number} до {max_number}"
        if value < min_number or value > max_number:
            raise ValueError(text_error)

    def add_grade(self, subject: str, grade: int):
        self.__is_valid_num(grade)
        self.__is_valid_grade(grade)
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        self.subjects[subject]["grade"] = grade

    def get_average_grade(self):
        sum_grades = 0
        count = 0
        for i in self.subjects.values():
            if i["grade"]:
                sum_grades += i["grade"]
                count += 1
        return sum_grades / count

    @staticmethod
    def __is_valid_test_score(value, min_number=0, max_number=100):
        text_error = (
            f"Результат теста должен быть целым числом от {min_number} до {max_number}"
        )
        if value < min_number or value > max_number:
            raise ValueError(text_error)

    def add_test_score(self, subject, test_score):
        self.__is_valid_num(test_score)
        self.__is_valid_test_score(test_score)
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        self.subjects[subject]["test_score"] = test_score

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        return float(self.subjects[subject]["test_score"])

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(subj for subj in self.subjects if (self.subjects[subj]['grade'] or self.subjects[subj]['test_score']))}"


# # test 1
# student = Student("Иван Иванов", "subjects.csv")
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
# student.add_grade("История", 5)
# student.add_test_score("История", 92)
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
# print(student)
# """
# Ожидаемый ответ:
# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История
# """

# # test 2
# student = Student("123 Иван", "subjects.csv")
# '''
# Ожидаемый ответ:
# ValueError: ФИО должно состоять только из букв и начинаться с заглавной буквы
# '''

# # test 3
# student = Student("Петров Петр", "subjects.csv")
# student.add_grade("Физика", 6)
# '''
# Ожидаемый ответ:
# ValueError: Оценка должна быть целым числом от 2 до 5
# '''

# # test 4
# student = Student("Сидоров Сидор", "subjects.csv")
# average_history_score = student.get_average_test_score("Биология")
# '''
# Ожидаемый ответ:
# ValueError: Предмет Биология не найден
# '''
