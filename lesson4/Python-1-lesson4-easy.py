# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print('Задача-1')

number_list = [1, 2, 4, 0]
new_number_list = [number**2 for number in number_list]
print(new_number_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('')
print('Задача-2')

fruits_1 = ['яблоко', 'банан', 'яблоко', 'киви', 'манго']
fruits_2 = ['яблоко', 'киви', 'манго', 'киви']

intersection_list = [fruit for fruit in fruits_1 if fruit in fruits_2]
print(list(set(intersection_list)))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('')
print('Задача-3')

import random

n = int(input('Введите количество элементов исходного списка: '))

number_list = [random.randint(-100, 100) for _ in range(n)]
print(number_list)

new_number_list = [number for number in number_list if (number % 3 == 0 and number >= 0 and number % 4 != 0)]
print('Новый список:', '\n', new_number_list)
