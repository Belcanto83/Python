# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

print('Задача-1')

number_list = [2, -5, 8, 9, -25, 25, 4]
revised_list = []

for number in number_list:
    if number >= 0 and (math.sqrt(number) - int(math.sqrt(number))) == 0:
        revised_list.append(math.sqrt(number))
    else:
        continue

print(number_list)
print(revised_list)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('')
print('Задача-2')

date = '08.12.2017'

days_list = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое']  # и так далее до 31? Не факт.. Можно сделать как-то по-другому..
months_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:])

date_str = '{} {} {} года'.format(days_list[day-1], months_list[month-1], year)

print(date)
print(date_str)

# Больше не успел сделать :(