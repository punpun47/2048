import random

def create_board():
    """Create a 4x4 matrix of zeros"""
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    return board

def display_board(board):
    """print board to terminal"""
    for row in board:
        print(row)

def add_random_tile(board):
    """Randomly choose an empty position on board and replace the zero with two"""
    r, c = random.choice([(r,c) for r in range(4) for c in range(4) if board[r][c] == 0])
    board[r][c] = 2

def compress(board):
    """Push all non-zeros left"""
    for index, row in enumerate(board):
        new_row = [value for value in row if value != 0]
        for _ in range(4 - len(new_row)):
          new_row.append(0) 
        board[index] = new_row
    
    return board

def merge(board):
    """Combines any row adjacent pairs that are equal,
    making the left one equal to the combination, 
    and the right one equal to zero"""
    for row in board:
        j = 0
        while j < 3:
            if row[j] == row[j+1] and row[j] != 0:
                row[j] = row[j] * 2
                row[j+1] = 0
                j += 2 #skip next index
            else:
                j += 1

def slide_left(board):
    new_board = compress(board)
    merge(new_board)
    compress(new_board)
    return new_board

                





# testing

board = create_board()
add_random_tile(board)
add_random_tile(board)
add_random_tile(board)
display_board(board)








