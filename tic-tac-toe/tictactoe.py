import pandas as pd
df = pd.read_csv('init.csv')
print(df)

def get_cell(move):
    if move == 1: return df.iloc[0][0]
    if move == 2: return df.iloc[0][1]
    if move == 3: return df.iloc[0][2]
    if move == 4: return df.iloc[1][0]
    if move == 5: return df.iloc[1][1]
    if move == 6: return df.iloc[1][2]
    if move == 7: return df.iloc[2][0]
    if move == 8: return df.iloc[2][1]
    if move == 9: return df.iloc[2][2]


def set_cell(move, piece):
    if get_cell(move) not in ('x', 'o'):
        if move == 1: df.iloc[0][0] = piece
        if move == 2: df.iloc[0][1] = piece
        if move == 3: df.iloc[0][2] = piece
        if move == 4: df.iloc[1][0] = piece
        if move == 5: df.iloc[1][1] = piece
        if move == 6: df.iloc[1][2] = piece
        if move == 7: df.iloc[2][0] = piece
        if move == 8: df.iloc[2][1] = piece
        if move == 9: df.iloc[2][2] = piece
        return True
    else:
        return False


def has_won():
    row1 = get_cell(1) + get_cell(1) + get_cell(3)
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

won = has_won()
print(won)

while not has_won():
    # Main
    if active_user == user1:
        piece = 'x'
    else:
        piece = 'o'
    
    move = int(input("Enter move: "))
    if set_cell(move, piece):
        print("/n")
        print(df)

print("Sie haben gewonnen!")

    





#set_cell(5, piece)
#print(df)
#print(get_cell(5))
# if df.iloc[0] != dfw1.iloc[0].any(1):
#     print("Player won!")

# for row in df.to_string():
#print(df.iloc[2])

#print(df.iloc[0][1])
#print(df.iloc[0].to_string(header=False, ))

#print(df.loc[[0]])
#print(df.to_string())
