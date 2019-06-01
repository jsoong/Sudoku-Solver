# print the board to the screen
def display_board(board):
    # loop through each cell
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == 8:
                print(board[i][j])  # cause a new line at end of row
            else:
                print(str(board[i][j]) + " ", end="")

def SelectUnassignedVariable(board):
    # base case
    find = find_empty(board)
    # check for base case, if board is full (done)
    if not find:
        return True
    # some empty cell still remains (not done)
    else:
        row, col = find

    for i in range(1, 10):
        # only add legal positions
        if Inference(board, i, (row, col)):
            # if valid, add into board
            board[row][col] = i

            # try to finish solution recursively
            if SelectUnassignedVariable(board):
                return True

            # unable to find solution, reset to empty, backtrack
            board[row][col] = 0

    return False

# check board state is valid (forward checking)
def Inference(board, num, pos):
    # Check if row is legal
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check if column is legal
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Define boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Check if box is legal
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    # if it reaches this point, all checks ok, it's legal
    return True

# empty cells (unsolved)
def find_empty(board):
    # loop through each cell
    for i in range(len(board)):
        for j in range(len(board[0])):
            # if cell is empty, return the row and col
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def fileOutput_board(board):
    # write solution to file
    with open('SUDUKO_Output5B.txt', 'w') as boardOut:
        # loop through each cell & write the solution to file
        for i in range(len(board)):
            for j in range(len(board[0])):
                if j == 8:
                    boardOut.write(str(board[i][j]))
                    boardOut.write("\n")  # cause a new line at end of row
                else:
                    boardOut.write(str(board[i][j]) + " ")

    return None


# read in the input file as a 2D array
with open('SUDUKO_Input5B.txt') as file:
    board = [[int(digit) for digit in line.split()] for line in file]

# run the solving program
SelectUnassignedVariable(board)
# display solution to screen
display_board(board)
# output the solution to file
fileOutput_board(board)
