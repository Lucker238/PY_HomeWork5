#3. Создайте программу для игры в ""Крестики-нолики"".
field = range(1,10)
cells = {1,2,3,4,5,6,7,8,9}
def create_field(field):
    for i in range(3):
        print("-"*19)
        print('| ', field[0+i*3], " | ", field[1+i*3], " | ", field[2+i*3], " |" )
    print("-"*19)

def check_move(turn, xo):
    while True:
        try:
            temp = int(turn)
            while not 0 < temp < 10:
                print('Введите число от 1 до 9')
                temp = int(input(f"Введите {xo}: "))
                continue
            if not temp in cells:
                print('Эта позиция уже занята!')
                temp = int(input(f"Введите {xo}: "))
                continue
            cells.remove(temp)
            return True
        except ValueError:
            turn = input(f"Введите {xo}: ")
            continue

# def lets_play()






create_field(field)
print(check_move(input("Test: "),'X'))
