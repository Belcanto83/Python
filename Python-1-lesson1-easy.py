print('Задача-1')  # Задача-1

a = 10  # int
b = 1.1  # float
c = True  # bool
text = 'qwerty'  # string
my_list = [1, 2, 3, text]

print(a, b, c, text)
print('My list:', my_list)

########################################

print('')
print('Задача-2')  # Задача-2

name = input('Введите Ваше имя: ')
print('Здравствуйте,', name)

num = int(input('Пожалуйста, введите число 0..100: '))
num += 2
print('Ваше число + 2 = ', num)
print('Ваше число + 2 = ' + str(num))

############################################

print('')
print('Задача-3')  # Задача-3

print(name + ',')
age = int(input('Пожалуйста, укажите Ваш возраст: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
