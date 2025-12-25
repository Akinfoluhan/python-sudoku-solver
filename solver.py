# first, we define a function to validate the rules of the game
def is_valid(board, num, pos):

    # set row and column using pos tuple
    row, col = pos

    # check if the number is in the current row
    if num in board[row]:
        return False
    
    # check if the number is in the current column
    for i in range(len(board)):
        if board[i][col] == num:
            return False
        
    # check if the number is in the current 3x3 box
    # get starting position of the 3x3 box - determine whole largest multiple of 3 less than or equal to row and col
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3

    # iterate through the 3x3 box
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False
            
    # if the number is not found in the row, column, or box, it is valid
    return True

# next, we define a function to find an empty cell in the board
def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col) # it returns the cell's position as a tuple (row, col)
    return None


# sanity check
if __name__ == "__main__":
    test_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 7, 9, 9]
    ]

    print(is_valid(test_board, 5, (0,2))) # False
    print(is_valid(test_board, 4, (0,2))) # True

    print(find_empty(test_board)) # (0,2)