# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому 
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

def player_vs_player():
    table = int(input('Введите начальное количество конфет(от 100 до 3000): '))
    while not 100 <= table <= 3000:
        table = int(input("Попробуйте ещё раз(от 100 до 3000): "))
    turn = random.randint(1,2)
    print(f'Первым ходит Игрок под номером {turn}')
    while table > 0:
        print(f'На столе {table} конфет(ы)')
        step = 0
        if turn == 1:
            step = int(input('Ход Игрока 1: '))
            while not 0 < step < 29:
                print('Чисто должно быть от 1 до 28')
                step = int(input('Ход Игрока 1:'))
            while step > table:
                print('Нельзя взять конфет больше, чем на столе!')
                step = int(input('Ход Игрока 1:'))
            table -= step
            if not table:
                break
            turn += 1
        else:
            step = int(input('Ход Игрока 2: '))
            while not 0 < step < 29:
                print('Чисто должно быть от 1 до 28')
                step = int(input('Ход Игрока 2:'))
            while step > table:
                print('Нельзя взять конфет больше, чем на столе!')
                step = int(input('Ход Игрока 2:'))
            table -= step
            if not table:
                break
            turn -= 1
    print(f'Победил Игрок номер {turn}')

def player_vs_simpbot():
    table = int(input('Введите начальное количество конфет(от 100 до 3000): '))
    while not 100 <= table <= 3000:
        table = int(input("Попробуйте ещё раз(от 100 до 3000): "))
    dict_g = {1:input('Введите своё имя: '), 2: 'BotMan'}
    turn = random.randint(1,2)
    print(f'Первым ходит {dict_g[turn]}')
    while table > 0:
        print(f'На столе {table} конфет(ы)')
        step = 0
        if turn == 1:
            step = int(input(f'Ходит {dict_g[turn]}: '))
            while not 0 < step < 29:
                print('Чисто должно быть от 1 до 28')
                step = int(input(f'{dict_g[turn]}, подумай и ходи: '))
            while step > table:
                print('Нельзя взять конфет больше, чем на столе!')
                step = int(input(f'{dict_g[turn]}, подумай и ходи: '))
            table -= step
            if table:
                turn += 1
        else:
            if table < 29:
                step = table
            else:
                step = random.randint(1,28)
            print(f'Ходит {dict_g[turn]}: {step}')
            table -= step
            if table:
                turn -= 1
    print(f'Победил {dict_g[turn]}')

def player_vs_skynet():
    table = int(input('Введите начальное количество конфет(от 100 до 3000): '))
    while not 100 <= table <= 3000:
        table = int(input("Попробуйте ещё раз(от 100 до 3000): "))
    dict_g = {1:input('Введите своё имя: '), 2: 'SkyNet'}
    turn = random.randint(1,2)
    print(f'Первым ходит {dict_g[turn]}')
    while table > 0:
        print(f'На столе {table} конфет(ы)')
        step = 0
        if turn == 1:
            step = int(input(f'Ходит {dict_g[turn]}: '))
            while not 0 < step < 29:
                print('Чисто должно быть от 1 до 28')
                step = int(input(f'{dict_g[turn]}, подумай и ходи: '))
            while step > table:
                print('Нельзя взять конфет больше, чем на столе!')
                step = int(input(f'{dict_g[turn]}, подумай и ходи: '))
            table -= step
            if table:
                turn += 1
        else:
            if table < 29:
                step = table
            elif table % 29:
                step = table % 29
            else:
                step = random.randint(1,28)
            print(f'Ходит {dict_g[turn]}: {step}')
            table -= step
            if table:
                turn -= 1
    print(f'Победил {dict_g[turn]}')

print(
    'Добро пожаловать в игру с конфетами.\n'
    'На столе лежит какое-то количество конфет (для сложности количество конфет задается в начале игры)\n'
    'Каждый ход игрок должен за свой ход взять со стола от 1 до 28 конфет.\n'
    'Тот кто делает последний ход выигрывает.\n'
    'Возможны режимы игры друг с другом, с ботом и с \'умным\' ботом.\n'
    '1. Игра с другом\n'
    '2. Игра с легким ботом\n'
    '3. Игра с тяжелым ботом\n'
)
check = True
while check:
    try:
        mode = int(input('Впишите номер режима: '))
        if 0 < mode < 4:
            check = False  
            break  
        print('Введите число от 1 до 3')
    except ValueError:
        mode = int(input('Ошибка ввода. Введите число от 1 до 3: '))
if mode == 1:
    player_vs_player()
elif mode == 2:
    player_vs_simpbot()
else:
    player_vs_skynet()

        

