board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(x):
    find = find_empty(x)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(x, i, (row, col)):
            x[row][col] = i

            if solve(x):
                return True

            x[row][col] = 0

    return False


def valid(x, number, position):
    # Check row
    for i in range(len(x[0])):
        if x[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(x)):
        if x[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if x[i][j] == number and (i,j) != position:
                return False

    return True


def print_board(x):
    for i in range(len(x)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(x[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j != 8:
                print(str(x[i][j]) + " ", end="")
            else:
                print(x[i][j])


def find_empty(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i, j)

    return None

print_board(board)
solve(board)
print("\n\n")
print_board(board)
