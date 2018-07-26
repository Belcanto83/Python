# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

print('Задача-1')


class TownCar:

    def __init__(self, name, color, speed, is_police):
        self._name = name
        self.color = color
        self._speed = speed
        self._is_police = is_police

    def get_name(self):
        return self._name

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'поворот ' + direction


class SportCar:

    def __init__(self, name, color, speed, is_police):
        self._name = name
        self.color = color
        self._speed = speed
        self._is_police = is_police

    def get_name(self):
        return self._name

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'Поворот ' + direction


class WorkCar:

    def __init__(self, name, color, speed, is_police):
        self._name = name
        self.color = color
        self._speed = speed
        self._is_police = is_police

    def get_name(self):
        return self._name

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'Поворот ' + direction


class PoliceCar:

    def __init__(self, name, color, speed, is_police):
        self._name = name
        self.color = color
        self._speed = speed
        self._is_police = is_police

    def get_name(self):
        return self._name

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'Поворот ' + direction


TownCar_1 = TownCar('BMW i3', 'red', 120.00, False)
print(TownCar_1.get_name(), TownCar_1.go())
print(TownCar_1.get_name(), TownCar_1.turn('направо'))


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

print('')
print('Задача-2')


class Car:

    def __init__(self, name, color, speed):
        self._name = name
        self.color = color
        self._speed = speed

    def get_name(self):
        return self._name

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'поворот ' + direction


class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed)
        self._is_police = is_police


class SportCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed)
        self._is_police = is_police


class WorkCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed)
        self._is_police = is_police


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed)
        self._is_police = is_police


TownCar_2 = TownCar('MINI Cooper', 'black', 110.00, False)
print(TownCar_2.get_name(), TownCar_2.go())
print(TownCar_2.get_name(), TownCar_2.turn('налево'))
