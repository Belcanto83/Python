# Задача 1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os, sys, shutil


def remove_directory(path):
    try:
        os.rmdir(path)
        print('Папка успешно удалена!')
    except FileNotFoundError:
        print('Папка с данным именем не существует!')


def create_directory(path):
    try:
        os.mkdir(path)
        print('Папка успешно создана!')
    except FileExistsError:
        print('Папка с данным именем уже существует!')


if __name__ == '__main__':

    print('Задача-1')

    action = None
    directory = 'dir_{}'
    list_dir = [directory.format(i) for i in range(1, 10)]

    try:
        action = int(input(
        '1 - создать директории dir_1 - dir_9\n'
        '2 - удалить директории dir_1 - dir_9\n'
        'Выберите действие: '))
    except ValueError:
        print('Пожалуйста, введите цифру 1 или 2 !')
        sys.exit()

    if action != 1 and action != 2:
        print('Пожалуйста, введите цифру 1 или 2 !')
        sys.exit()

    if action == 1:
        for directory in list_dir:
            dir_path = os.path.join(os.getcwd(), directory)
            try:
                os.mkdir(dir_path)
            except FileExistsError:
                print('Папка с именем {} уже существует!'.format(directory))
                continue
    elif action == 2:
        for directory in list_dir:
            dir_path = os.path.join(os.getcwd(), directory)
            try:
                os.rmdir(dir_path)
            except FileNotFoundError:
                print('Папка с именем {} не существует!'.format(directory))
                continue


    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    print('')
    print('Задача-2')

    print(os.listdir(os.getcwd()))

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    print('')
    print('Задача-3')

    current_file_name = os.path.join(os.getcwd(), __file__)
    copy_file_name = os.path.join(os.getcwd(), 'copy_of_current_script.py')
    shutil.copyfile(current_file_name, copy_file_name)
    print('Файл скопирован!')
