# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import lesson5.python1_lesson5_easy as my_os_module


current_directory = os.getcwd()

while True:
    action = input(
        '1 - Перейти в папку\n'
        '2 - Просмотреть содержимое текущей папки\n'
        '3 - Удалить папку\n'
        '4 - Создать папку\n'
        '5 - Выход\n'
        'Выберите действие: ')

    if action == '1':
        current_directory = input('Введите путь к папке: ')
        try:
            os.chdir(current_directory)
            print('Успешно! Текущая директория:', os.getcwd())
        except FileNotFoundError:
            print('Вы указали неверный путь!')
    elif action == '2':
        print('Содержимое текущей директории', os.getcwd())
        for directory in os.listdir(current_directory):
            print(directory)
    elif action == '3':
        removed_directory = input('Введите путь к папке: ')
        my_os_module.remove_directory(removed_directory)
    elif action == '4':
        new_directory = input('Введите путь к папке: ')
        my_os_module.create_directory(new_directory)
    elif action == '5':
        break
    else:
        print('Пожалуйста, введите цифру 1 - 5 !')
