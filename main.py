import random
import os

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
    os.system('clear') # clears terminal after every move

    for row in board:
        print("[", end="")
        print(' '.join(f'{value:4}' for value in row), end="")
        print("]")

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

def reverse(board):
    """Reverse the rows of the board - to use for slide right function"""
    for index, row in enumerate(board):
        row.reverse()
        board[index] = row

def transpose(board):
    """Get the transpose of the matrix - to use for slide up/down function"""
    transposed_matrix = [[row[i] for row in board]for i in range(4)]
    return transposed_matrix


def slide_left(board):
    compress(board)
    merge(board)
    compress(board)


def slide_right(board):
    reverse(board)
    slide_left(board)
    reverse(board)

def slide_up(board):
    matrix = transpose(board)
    slide_left(matrix)
    matrix = transpose(matrix)
    for i in range(4):
        board[i] = matrix[i]


def slide_down(board):
    matrix = transpose(board)
    slide_right(matrix)
    matrix = transpose(matrix)
    for i in range(4):
        board[i] = matrix[i]

def get_user_move(board):
    old_board = [row[:] for row in board] # copy before move
    user_input = input("Please enter w,a,s,d: ")
    if user_input.capitalize() == "W":
        slide_up(board)
    elif user_input.capitalize() == "A":
        slide_left(board)
    elif user_input.capitalize() == "S":
        slide_down(board)
    elif user_input.capitalize() == "D":
        slide_right(board)
    return board != old_board # True only if something changed


def is_game_over(board):
    # check for empty cells
    if len([(r,c) for r in range(4) for c in range(4) if board[r][c] == 0]) != 0:
        return False
    # check horizontal neighbours
    for r in range(4):
        for c in range(3):
            if board[r][c] == board[r][c+1]:
                return False
            
    # check vertical neighbours
    for r in range(3):
        for c in range(4):
            if board[r][c] == board[r+1][c]:
                return False
            
    return True
    




def main():
    print("-------------Welcome to 2048-------------")
    print("use wasd to move")
    
    board = create_board()
    add_random_tile(board)
    add_random_tile(board)
    while True:
        display_board(board)
        if is_game_over(board):
            print("GAME OVER")
            return
        
        if get_user_move(board):
            add_random_tile(board) #Only add a random tile if User moves successfully





if __name__ == "__main__":
    main()



                










