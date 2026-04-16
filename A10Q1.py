def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row, solutions):
    if row == 8:  
        solutions.append(board[:])
        return
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col 
            solve(board, row + 1, solutions)  
            board[row] = -1 

def print_solution(board):
    for row in board:
        line = ['Q' if col == board.index(row) else '.' for col in range(8)]
        print(" ".join(line))

def eight_queens():
    board = [-1] * 8 
    solutions = []
    solve(board, 0, solutions)  
    
    print(f"Total solutions: {len(solutions)}")
    for solution in solutions:
        print_solution(solution)
        print()

eight_queens()
