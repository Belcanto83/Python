import random


class Card:

    def __init__(self, name):
        self._name = name
        self._card_rows = 3
        self._numbers_in_row = 5
        self._numbers_qty_on_card = self._card_rows * self._numbers_in_row
        self._cell_qty_in_row = 9
        self._number_list = []
        self._cells = []
        # создаем список случайных чисел (1 - 90) на карточке  и записываем его в атрибут _number_list
        self.generate_number_list()
        self.card_string = self.return_card_string()

    # создаем список случайных чисел (1 - 90) на карточке  и записываем его в атрибут _number_list
    def generate_number_list(self):
        while len(self._number_list) < self._numbers_qty_on_card:
            number = random.randint(1, 90)
            if number not in self._number_list:
                self._number_list.append(number)

    # распределяем числовые значения из списка по строкам карточки
    def assign_numbers_to_rows(self):
        one_row_numbers = []
        all_rows_numbers = []
        number_list_copy = self._number_list[:]
        while len(all_rows_numbers) < self._card_rows:
            while len(one_row_numbers) < self._numbers_in_row:
                number = random.choice(number_list_copy)
                one_row_numbers.append(number)
                number_list_copy.remove(number)
            all_rows_numbers.append(one_row_numbers)
            one_row_numbers = []
        return all_rows_numbers

    # определяем номера ячеек строки карточки, которые будут заполнены числовыми значениями
    def filled_cells_in_row(self):
        filled_cells = []
        all_rows_filled_cells = []
        cell_numbers = list(range(self._cell_qty_in_row))
        while len(all_rows_filled_cells) < self._card_rows:
            while len(filled_cells) < self._numbers_in_row:
                number = random.choice(cell_numbers)
                filled_cells.append(number)
                cell_numbers.remove(number)
            all_rows_filled_cells.append(filled_cells)
            filled_cells = []
            cell_numbers = list(range(self._cell_qty_in_row))
        return all_rows_filled_cells

    # сортируем числовые значения в строке карточки по возрастанию, формируем карточку и показываем ее
    def return_card_string(self):
        card_string = self._name.center(3 * self._cell_qty_in_row, '-')
        card_string += '\n'
        rows = self.assign_numbers_to_rows()
        filled_cells_numbers_list = self.filled_cells_in_row()
        for j in range(self._card_rows):
            row = rows[j]
            filled_cells_numbers = filled_cells_numbers_list[j]
            min_number_in_row = min(row)
            for cell_number in range(self._cell_qty_in_row):
                if cell_number in filled_cells_numbers:
                    card_string += str(min_number_in_row).rjust(2) + ' '
                    row.remove(min_number_in_row)
                    try:
                        min_number_in_row = min(row)
                    except ValueError:
                        pass
                else:
                    card_string += '   '
            card_string += '\n'
        return card_string

    def check_number_in_card(self, number):
        if number in self._number_list:
            if number > 9:
                self.card_string = self.card_string.replace(str(number), '--')
            else:
                self.card_string = self.card_string.replace(' ' + str(number) + ' ', '-- ')
            self._number_list.remove(number)


class Game:

    def __init__(self, player_card, computer_card):
        self._player_card = player_card
        self._computer_card = computer_card
        self._numbers_set = list(range(1, 91))

    def start(self):
        winner = None
        while not winner:
            number = random.choice(self._numbers_set)
            self._numbers_set.remove(number)
            print('Новый бочонок:', number, ',', 'Осталось бочонков:', len(self._numbers_set))
            print(self._player_card.card_string)
            print(self._computer_card.card_string)
            answer = input('Зачеркнуть цифру? (y/n): ')
            self._computer_card.check_number_in_card(number)
            if answer == 'y' and number in self._player_card._number_list:
                self._player_card.check_number_in_card(number)
            elif answer == 'y' and number not in self._player_card._number_list:
                winner = self._computer_card
                break
            elif answer == 'n' and number not in self._player_card._number_list:
                self._player_card.check_number_in_card(number)
            elif answer == 'n' and number in self._player_card._number_list:
                winner = self._computer_card
            else:
                winner = self._computer_card
            #########################################
            if len(self._computer_card._number_list) == 0 and len(self._player_card._number_list) == 0:
                winner = None
                break
            elif len(self._computer_card._number_list) == 0:
                winner = self._computer_card
            elif len(self._player_card._number_list) == 0:
                winner = self._player_card
        if winner == self._computer_card:
            print('Победил компьютер!')
        elif winner == self._player_card:
            print('Победил игрок!')
        else:
            print('Ничья!')




player_card = Card('Моя карта')
computer_card = Card('Карта компьютера')

game_loto = Game(player_card, computer_card)
game_loto.start()
