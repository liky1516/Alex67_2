# FPW-117 Ткач Александр Георгиевич
# 05.04.2023 г.
# ИТОГОВОЕ ЗАДАНИЕ 6.6 (HW-02)
import sys
Start_Board = {1:'-', 2:'-', 3:'-', 4:'-', 5:'-', 6:'-', 7:'-', 8:'-', 9:'-'}  # игровое поле

# Список списков выигрышных ситуаций
Win_case = [[1, 2, 3], [4, 5, 6], [7, 8, 9],  # строки
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # столбцы
            [1, 5, 9], [3, 5, 7]              # диагонали
            ]

useful_bits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # варианты нажатых клавиш
n = 9  # счетчик ходов
L_x = []  # список нажатых клавиш крестиков (Х)
L_o = []  # список нажатых клавиш ноликов (О)


# функция печати поля
def p_board():
    print(f'{Start_Board[7]} {Start_Board[8]} {Start_Board[9]}')
    print(f'{Start_Board[4]} {Start_Board[5]} {Start_Board[6]}')
    print(f'{Start_Board[1]} {Start_Board[2]} {Start_Board[3]}')


# Функция опроса клавы и в случае нажатия из списка useful_bits, запоминаем
# нажатую цифру в списке L_x
# а также перезаписываем поле
def running_X():
    x_ = int(input('Ходят Х [1-9]; [0] - выход :'))
    while x_ not in useful_bits:
        x_ = int(input('Ходят Х [1-9]; [0] - выход :'))
        if x_ == 0:
            sys.exit()

    if Start_Board[x_] == '-':  # проверка пустая ли клетка
        Start_Board[x_] = 'X'
        L_x.append(x_)
        global n
        n -= 1  # количество ходов уменьшается
        p_board()
        return (n)
    else:
        print('Клетка занята, повторите ввод')
        running_X()


# такая же функция, только для ноликов
def running_O():
    o_ = int(input('Ходят O [1-9]; [0] - выход :'))
    while o_ not in useful_bits:
        o_ = int(input('Ходят O [1-9]; [0] - выход :'))
        if o_ == 0:
            sys.exit()
    if Start_Board[o_] == '-':  # проверка пустая ли клетка
        Start_Board[o_] = 'O'
        L_o.append(o_)
        global n
        n -= 1  # количество ходов уменьшается
        p_board()
        return (n)
    else:
        print('Клетка занята, повторите ввод')
        running_O()

p_board()
while n:  # пока есть ходы
    running_X()  # запуск хода крестиков
    L_x_set = set(L_x)
    for k in Win_case:  # последовательно берем выигрышные ситуации
        if len(L_x_set.intersection(set(k))) == 3:  # проверяем, что бы было три совпадения с эталоном
            print('ПОБЕДА КРЕСТИКОВ! УРА!!')
            sys.exit()

    if not n:
        print('ДРУЖЕСТВЕННАЯ НИЧЬЯ..')

    running_O()  # запуск хода ноликов
    L_o_set = set(L_o)
    for k in Win_case:  # последовательно берем выигрышные ситуации
        if len(L_o_set.intersection(set(k))) == 3:  # проверяем, что бы было три совпадения с эталоном
            print('ПОБЕДА НОЛИКОВ! УРА!!!')
            sys.exit()

    if not n:
        print('ДРУЖЕСТВЕННАЯ НИЧЬЯ..')




