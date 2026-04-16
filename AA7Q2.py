import random
import math

# -------------------------------------------------
# BOARD REPRESENTATION
# board[i] = row position of the queen in column i
# Example: board = [0,4,7,5,2,6,1,3]
# -------------------------------------------------

# -------------------------------------------------
# HEURISTIC FUNCTION
# h(board) = number of attacking queen pairs
# Goal: minimize h(board) to 0
# -------------------------------------------------
def h(board):
    conflicts = 0

    # Check all unique queen pairs
    for i in range(8):
        for j in range(i + 1, 8):

            # Same row conflict
            if board[i] == board[j]:
                conflicts += 1

            # Diagonal conflict
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# -------------------------------------------------
# STEEPEST-ASCENT HILL CLIMBING
# Used by Random-Restart Hill Climbing
# -------------------------------------------------
def steepest(board):
    steps = 0

    while True:
        neighbors = []

        # Generate all neighbors
        # Move one queen in its column to every other row
        for col in range(8):
            for row in range(8):
                if row != board[col]:
                    new_board = board[:]
                    new_board[col] = row
                    neighbors.append(new_board)

        # Select neighbor with minimum heuristic value
        next_board = min(neighbors, key=h)

        # Stop if no improvement (local minimum reached)
        if h(next_board) >= h(board):
            break

        # Move to better neighbor
        board = next_board
        steps += 1

        # Stop if solution found
        if h(board) == 0:
            break

    return board, h(board), steps


# -------------------------------------------------
# FIRST-CHOICE HILL CLIMBING
# Accepts the first improving move found
# -------------------------------------------------
def first_choice(board):
    steps = 0

    # Limit steps to avoid infinite loops
    while h(board) != 0 and steps < 100:
        improved = False

        # Try moving queens column by column
        for col in range(8):

            # Random row order to reduce determinism
            for row in random.sample(range(8), 8):
                if row != board[col]:
                    new_board = board[:]
                    new_board[col] = row

                    # Accept first better move
                    if h(new_board) < h(board):
                        board = new_board
                        steps += 1
                        improved = True
                        break

            if improved:
                break

        # Stop if no improving move exists (local minimum)
        if not improved:
            break

    return board, h(board), steps


# -------------------------------------------------
# RANDOM-RESTART HILL CLIMBING
# Runs steepest ascent from multiple random starts
# -------------------------------------------------
def random_restart(board=None):

    # Try 50 random initial boards
    for _ in range(50):

        # Generate random board
        board = [random.randint(0, 7) for _ in range(8)]

        # Run steepest ascent from this board
        final_board, final_h, steps = steepest(board)

        # Stop immediately if solution found
        if final_h == 0:
            return final_board, final_h, steps

    # Return last attempt if no solution
    return final_board, final_h, steps


# -------------------------------------------------
# SIMULATED ANNEALING
# Allows occasional worse moves to escape local minima
# -------------------------------------------------
def simulated_annealing(board):
    steps = 0
    T = 100   # Initial temperature

    while h(board) != 0 and steps < 1000:

        # Select random queen and random row
        col = random.randint(0, 7)
        row = random.randint(0, 7)

        if row != board[col]:
            new_board = board[:]
            new_board[col] = row

            delta = h(new_board) - h(board)

            # Accept move if better OR with probability if worse
            if delta < 0 or random.random() < math.exp(-delta / T):
                board = new_board

        # Reduce temperature gradually
        T *= 0.95
        steps += 1

    return board, h(board), steps


# -------------------------------------------------
# EXPERIMENT: RUN EACH ALGORITHM ON 50 RANDOM BOARDS
# -------------------------------------------------
random.seed(42)  # Ensures repeatable results

algorithms = [
    ("First-Choice", first_choice),
    ("Random-Restart", random_restart),
    ("Simulated Annealing", simulated_annealing)
]

for name, algo in algorithms:
    solved = 0
    total_steps = 0

    print(f"\n{name}")
    print("InitH | FinalH | Steps | Status")

    for _ in range(50):

        # Generate random initial board
        board = [random.randint(0, 7) for _ in range(8)]
        init_h = h(board)

        # Run selected algorithm
        final_board, final_h, steps = algo(board[:])

        # Check success
        status = "Solved" if final_h == 0 else "Fail"

        if final_h == 0:
            solved += 1

        total_steps += steps

        print(f"{init_h:>5} | {final_h:>6} | {steps:>5} | {status}")

    print(f"Success Rate: {solved}/50, Avg Steps: {total_steps/50:.2f}")
    