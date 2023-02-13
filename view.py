def get_op():
    op = int(input("1- Добавление нового студента:\n 2-Добавление предмета:\n 3-Добавление оценки ученику по предмету:\n 4-Показ списка учеников (имена фамилия):\n 5- Показ листа оценок конкретного ученика:\n 6-Выход из программы\n"))
    return op

def add_student():
    name = input("Введите Имя и Фамилию ученика: ")
    return name

def add_lesson():
    less= input("Введите наименование предмета: ")
    return less

def imput_mark():
    name = input("Введите Имя и Фамилию: ")
    less = input("Введите предмет: ")
    mark = input("Введите Оценку: ")
    return name, less, mark

def get_name_and_mark():
    name = input("Введите имя и Фамилию ученика: ")
    return name
