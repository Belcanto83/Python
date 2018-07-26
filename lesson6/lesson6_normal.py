# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, enemy):
        enemy.health -= self.damage // enemy.armor
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(self.name, enemy.name,
                                                                        self.damage, enemy.health))
        return enemy.health


class StartFightingGame:

    def start_game(self, attacker_1, attacker_2, last_attacker):
        while attacker_1.health > 0 and attacker_2.health > 0:
            if last_attacker == attacker_1:
                attacker_2.attack(attacker_1)
                last_attacker = attacker_2
            else:
                attacker_1.attack(attacker_2)
                last_attacker = attacker_1

        if attacker_1.health > 0:
            print('{} победил!'.format(attacker_1.name))
        else:
            print('{} победил!'.format(attacker_2.name))


player_name = input('Введите свое имя: ')
enemy_name = input('Введите имя соперника: ')

player = Person(player_name, 55, 30, 1.0)
enemy = Person(enemy_name, 80, 25, 1.0)

game_1 = StartFightingGame()
game_1.start_game(player, enemy, enemy)
