# Задача-1: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

print('Задача-1')  # Задача-1

loop_control = True
num = 0

while loop_control:
    num = float(input('Пожалуйста, введите число от 0 до 10: '))

    if 0 <= num <= 10:
        num **= 2
        loop_control = False
    else:
        print('Пожалуйста, введите число в заданном диапазоне!')

print('Ваше число в квадрате: ' + str(num))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

print('')
print('Задача-2')  # Задача-2

# Решение подходит для типов данных 'float' и 'integer';  для типа данных 'string' не подходит!

a = float(input('Пожалуйста, введите первое число: '))
b = float(input('Пожалуйста, введите второе число: '))

print('a =', a, ' b = ', b)

a = a + b
b = a - b
a = a - b

print('a =', a, ' b = ', b)
