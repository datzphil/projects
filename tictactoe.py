# write your code here
def grid(value):
    print("---------")
    print("|" + " " + value[0] + " " + value[1] + " " + value[2] + " " + "|")
    print("|" + " " + value[3] + " " + value[4] + " " + value[5] + " " + "|")
    print("|" + " " + value[6] + " " + value[7] + " " + value[8] + " " + "|")
    print("---------")


result = "         "
listed = list(result)
grid(result)

# possible choices
row1 = listed[0] + listed[1] + listed[2]
row2 = listed[3] + listed[4] + listed[5]
row3 = listed[6] + listed[7] + listed[8]
rows = [row1, row2, row3]

column1 = listed[0] + listed[3] + listed[6]
column2 = listed[1] + listed[4] + listed[7]
column3 = listed[2] + listed[5] + listed[8]
columns = [column1, column2, column3]

diagonal1 = listed[0] + listed[4] + listed[8]
diagonal2 = listed[2] + listed[4] + listed[6]
diagonals = [diagonal1, diagonal2]

total = rows + columns + diagonals


def next_move_x(cell):
    coordinates = cell.split()
    if coordinates[0] not in ["1", "2", "3"]:
        print("Coordinates should be from 1 to 3")
        next_move_x(input())
    elif coordinates[1] not in ["1", "2", "3"]:
        print("Coordinates should be from 1 to 3")
        next_move_x(input())
    elif coordinates[0] == "1":
        if coordinates[1] == "1":
            if listed[6] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[6] = "X"
                grid(listed)
        elif coordinates[1] == "2":
            if listed[3] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[3] = "X"
                grid(listed)
        elif coordinates[1] == "3":
            if listed[0] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[0] = "X"
                grid(listed)
    elif coordinates[0] == "2":
        if coordinates[1] == "1":
            if listed[7] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[7] = "X"
                grid(listed)
        elif coordinates[1] == "2":
            if listed[4] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[4] = "X"
                grid(listed)
        elif coordinates[1] == "3":
            if listed[1] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[1] = "X"
                grid(listed)
    elif coordinates[0] == "3":
        if coordinates[1] == "1":
            if listed[8] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[8] = "X"
                grid(listed)
        elif coordinates[1] == "2":
            if listed[5] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[5] = "X"
                grid(listed)
        elif coordinates[1] == "3":
            if listed[2] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_x(input())
            else:
                listed[2] = "X"
                grid(listed)


def next_move_o(cell):
    coordinates = cell.split()
    if coordinates[0] not in ["1", "2", "3"]:
        print("Coordinates should be from 1 to 3")
        next_move_o(input())
    elif coordinates[1] not in ["1", "2", "3"]:
        print("Coordinates should be from 1 to 3")
        next_move_o(input())
    elif coordinates[0] == "1":
        if coordinates[1] == "1":
            if listed[6] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[6] = "O"
                grid(listed)
        elif coordinates[1] == "2":
            if listed[3] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[3] = "O"
                grid(listed)
        elif coordinates[1] == "3":
            if listed[0] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[0] = "O"
                grid(listed)
    elif coordinates[0] == "2":
        if coordinates[1] == "1":
            if listed[7] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[7] = "O"
                grid(listed)
        elif coordinates[1] == "2":
            if listed[4] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[4] = "O"
                grid(listed)
        elif coordinates[1] == "3":
            if listed[1] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[1] = "O"
                grid(listed)
    elif coordinates[0] == "3":
        if coordinates[1] == "1":
            if listed[8] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[8] = "O"
                grid(listed)
        elif coordinates[1] == "2":
            if listed[5] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[5] = "O"
                grid(listed)
        elif coordinates[1] == "3":
            if listed[2] == ("X" or "O"):
                print("This cell is occupied! Choose another one!")
                next_move_o(input())
            else:
                listed[2] = "O"
                grid(listed)


x_count = 0
o_count = 0

while ("XXX" not in total) or ("OOO" not in total) or (" " not in total):

    row1 = listed[0] + listed[1] + listed[2]
    row2 = listed[3] + listed[4] + listed[5]
    row3 = listed[6] + listed[7] + listed[8]
    rows = [row1, row2, row3]

    column1 = listed[0] + listed[3] + listed[6]
    column2 = listed[1] + listed[4] + listed[7]
    column3 = listed[2] + listed[5] + listed[8]
    columns = [column1, column2, column3]

    diagonal1 = listed[0] + listed[4] + listed[8]
    diagonal2 = listed[2] + listed[4] + listed[6]
    diagonals = [diagonal1, diagonal2]

    total = rows + columns + diagonals

    if "XXX" in total:
        print("X wins")
        break
    if "OOO" in total:
        print("O wins")
        break
    if x_count == 5 or o_count == 5:
        print("Draw")
        break
    if o_count < x_count:
        next_move_o(input())
        o_count += 1
        if "XXX" in total:
            print("X wins")
            break
    elif o_count == x_count:
        next_move_x(input())
        x_count += 1
        if "OOO" in total:
            print("O wins")
            break
