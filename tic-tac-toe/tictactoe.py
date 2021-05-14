import pandas as pd
import os

df = pd.read_csv('init.csv')


def get_cell(my_move):
    if my_move == 1: return df.iloc[0][0]
    if my_move == 2: return df.iloc[0][1]
    if my_move == 3: return df.iloc[0][2]
    if my_move == 4: return df.iloc[1][0]
    if my_move == 5: return df.iloc[1][1]
    if my_move == 6: return df.iloc[1][2]
    if my_move == 7: return df.iloc[2][0]
    if my_move == 8: return df.iloc[2][1]
    if my_move == 9: return df.iloc[2][2]
    else:
        return 'wrong'


def set_cell(my_move, my_piece):
    if get_cell(move) not in ('x', 'o', 'wrong'):
        if my_move == 1: df.iloc[0][0] = my_piece
        if my_move == 2: df.iloc[0][1] = my_piece
        if my_move == 3: df.iloc[0][2] = my_piece
        if my_move == 4: df.iloc[1][0] = my_piece
        if my_move == 5: df.iloc[1][1] = my_piece
        if my_move == 6: df.iloc[1][2] = my_piece
        if my_move == 7: df.iloc[2][0] = my_piece
        if my_move == 8: df.iloc[2][1] = my_piece
        if my_move == 9: df.iloc[2][2] = my_piece
        return True
    else:
        return False


def has_won():
    row1 = get_cell(1) + get_cell(2) + get_cell(3)
    if row1 in ('xxx', 'ooo'): return True
    row2 = get_cell(4) + get_cell(5) + get_cell(6)
    if row2 in ('xxx', 'ooo'): return True
    row3 = get_cell(7) + get_cell(8) + get_cell(9)
    if row3 in ('xxx', 'ooo'): return True
    col1 = get_cell(1) + get_cell(4) + get_cell(7)
    if col1 in ('xxx', 'ooo'): return True
    col2 = get_cell(2) + get_cell(5) + get_cell(8)
    if col2 in ('xxx', 'ooo'): return True
    col3 = get_cell(3) + get_cell(6) + get_cell(9)
    if col3 in ('xxx', 'ooo'): return True
    cross1 = get_cell(1) + get_cell(5) + get_cell(9)
    if cross1 in ('xxx', 'ooo'): return True
    cross2 = get_cell(7) + get_cell(5) + get_cell(3)
    if cross2 in ('xxx', 'ooo'): return True
    else:
        return False


user1 = 'Player 1'  # input("Enter Name1: ")
user2 = 'Player 2'  # input("Enter Name1: ")
active_user = user1
all_moves = [i for i in range(1, 10)]

while not has_won():
    # Main
    if active_user == user1:
        piece = 'x'
    else:
        piece = 'o'

    print(df)

    try:
        move = int(input("Enter move " + active_user + ': '))

    except:
        print("This move is not possible, please try again")
        print(all_moves)

    if set_cell(move, piece):
        print("Move successful.")
        all_moves.remove(move)

        if has_won():
            print(df)
            print("***** You won! *****")
            break

        elif not all_moves:
            print(df)
            print("===== Draw! =====")
            break

        if active_user == user1:
            active_user = user2
        else:
            active_user = user1

    else:
        print("This move is not possible, please try again")
        print(all_moves)
