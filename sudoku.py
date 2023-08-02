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
        return True    #board is completed solved
    else:
        row, col = find

    for i in range(1,10):
        if valid(x, i, (row, col)):
            x[row][col] = i

            #backtracking (recursion)
            if solve(x):
                return True    #acceptable solution if found for next empty cell

            #if next acceptable solution is not found, cell value is set back to zero
            x[row][col] = 0

    return False


# takes in board, (in loop for numbers 1 to 9), and given empty cell
# checks board and returns true if an acceptable solution is found, else returns false
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

# printing cleaned up version of board
def print_board(x):
    for i in range(len(x)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(x[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j != 8:
                print(str(x[i][j]) + " ", end="")
            else:
                print(x[i][j])

# takes in board, uses length and width of board to find the next empty cell on board
# if empty cell is found, it is returned, else returns NONE
def find_empty(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i, j)

    return None

print("\n")
print_board(board)
print("\n\n")
if solve(board):
    print_board(board)
else:
    print("Board cannot be solved.")
