#3. Создайте программу для игры в ""Крестики-нолики"".
field = [1,2,3,4,5,6,7,8,9]
cells = {1,2,3,4,5,6,7,8,9}
win_possitions = [{1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7}]
def create_field(field):
    for i in range(3):
        print('| ', field[0+i*3], " | ", field[1+i*3], " | ", field[2+i*3], " |" )
        if i == 2:
            break
        print('-'*19)


def check_move(move, xo: str):
    while True:
        try:
            temp = int(move)
            if not 0 < temp < 10:
                print('Введите число от 1 до 9')
                move = int(input(f"Введите {xo}: "))
                continue
            if not temp in cells:
                print('Эта позиция уже занята!')
                move = int(input(f"Введите {xo}: "))
                continue
            cells.remove(temp)
            return temp
        except ValueError:
            print('Вы ввели какую то ерунду!')
            move = input(f"Введите {xo}: ")
            continue

def check_win(array: list):
    win_possitions = [{1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7}]
    for win_poss in win_possitions:
        for game_poss in array:
            if len(win_poss):
                if game_poss in win_poss:
                    win_poss.remove(game_poss)
            else:
                return True
        if not len(win_poss):
            return True
    return False

def lets_play():
    create_field(field)
    xo = {1:"X", 0:'O'}
    turn = 1
    x_poss = []
    y_poss = []
    while turn <= 9:
        if turn % 2:
            x = str(xo[turn%2])
            move = check_move(input(f'Введите {xo[turn%2]}: '), x)
            x_poss.append(move)
            field[field.index(move)] = xo[turn%2]
            create_field(field)
            if check_win(x_poss):
                print('Победили крестики! Поздравляю!')
                return 
            turn += 1
        else:
            y = str(xo[turn%2])
            move = check_move(input(f'Введите {xo[turn%2]}: '), y)
            y_poss.append(move)
            field[field.index(move)] = xo[turn%2]
            create_field(field)
            if check_win(y_poss):
                print('Победили нолики! Поздравляю!')
                return 
            turn += 1           
    else:
        print('У вас ничья!')
        return 

lets_play()