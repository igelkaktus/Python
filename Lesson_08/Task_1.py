'''
== Лото == Сдать до 24 сент., 20:00 +03:00

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
'''

import random, sys

# Формирование карточек

ballsleft = 90
p1 = 15
p2 = 15
balls = random.sample(range(1, 91), 90) #Набор бочонков для игры
game_set = random.sample(range(1, 90), 30)  # Набор случайных чисел для двух карточек
p1_set = random.sample(game_set, 15)  # Набор Чисел для 1-й карточки
p2_set = [e for e in game_set if not e in p1_set]  # Набор чисел для 2-й карточки
p1_card = [p1_set[:5], p1_set[5:10], p1_set[10:]] #Строки для 1-й карточки
p2_card = [p2_set[:5], p2_set[5:10], p2_set[10:]] #Строки для 2-й карточки
for p1line in p1_card:
    p1line.sort()  # Сортировка по возрастанию
    p1line.insert(random.randint(0, 4), ' ')  # Вставка пустых клеток
    p1line.insert(random.randint(0, 5), ' ')
    p1line.insert(random.randint(0, 6), ' ')
    p1line.insert(random.randint(0, 7), ' ')
for p2line in p2_card:
    p2line.sort()
    p2line.insert(random.randint(0, 4), ' ')
    p2line.insert(random.randint(0, 5), ' ')
    p2line.insert(random.randint(0, 6), ' ')
    p2line.insert(random.randint(0, 7), ' ')


def card(p):
    if p == 0:
        print('{:-^26}'.format(' Your Card '))
        for line1 in p1_card:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p == 1:
        print('{:-^26}'.format(' Computer\'s card '))
        for line2 in p2_card:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


def your_move(): #Ход игрока
    a = input('Strike out the number? (y/n): ')
    if a == 'y':
        if ball in p1_set:
            for l in p1_card:
                try:
                    l.insert(l.index(ball), '><')
                    l.pop(l.index(ball))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nGAME OVER')
            sys.exit()
    if a == 'n':
        if ball in p1_set:
            print('\nGAME OVER')
            sys.exit()
        else:
            print('\nOK')


def comp_move(): #Ход компьютера
    if ball in p2_set:
        for i in p2_card:
            try:
                i.insert(i.index(ball), '><')
                i.pop(i.index(ball))
            except ValueError:
                continue
        return 1


for ball in balls:
    ballsleft -= 1
    print('\nNew ball: {} ( {} left)\n'.format(ball, ballsleft))
    card(0)
    card(1)
    if your_move() == 1:
        p1 -= 1
    if comp_move() == 1:
        p2 -= 1
    if p1 == 0:
        print('\nYOU WON')
        sys.exit()
    if p2 == 0:
        print('\nYOU LOST')
        sys.exit()
    if ballsleft == 0:
        print('\nGAME OVER')
        sys.exit()
