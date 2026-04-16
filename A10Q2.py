import random

def is_valid(board):
    for row1 in range(8):
        for row2 in range(row1 + 1, 8):
            col1 = board[row1]
            col2 = board[row2]
            if col1 == col2 or abs(col1 - col2) == abs(row1 - row2):
                return False
    return True

def random_queen_placement():
    board = random.sample(range(8), 8)  
    return board

def solve_randomly():
    attempts = 0
    while True:
        attempts += 1
        board = random_queen_placement()
        if is_valid(board):
            return board, attempts

def print_board(board):
    for row in range(8):
        row_str = ['.' for _ in range(8)]
        row_str[board[row]] = 'Q'
        print(' '.join(row_str))

def find_solution():
    solution, attempts = solve_randomly()
    print(f"Found a valid solution after {attempts} attempts:\n")
    print_board(solution)

find_solution()
