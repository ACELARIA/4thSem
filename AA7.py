import random   # Used to generate random initial boards

# --------------------------------------------------
# Heuristic function
# Counts the number of attacking queen pairs
# Lower value = better state
# h(board) = 0 means a valid solution
# --------------------------------------------------
def h(board):
    return sum(
        1                                  # Count one conflict
        for i in range(8)                 # First queen (column i)
        for j in range(i + 1, 8)           # Second queen (column j), avoid double counting
        if (
            board[i] == board[j]           # Same row conflict
            or abs(board[i] - board[j])    # Diagonal conflict:
            == abs(i - j)                  # |row difference| == |column difference|
        )
    )


# --------------------------------------------------
# Steepest-Ascent Hill Climbing Algorithm
# --------------------------------------------------
def steepest(board):
    steps = 0                              # Number of moves taken

    while True:
        neighbors = []                    # List to store all neighboring boards

        # Generate all neighbors
        # Move one queen at a time to every other row
        for col in range(8):              # Fix a column
            for row in range(8):          # Try all rows
                if row != board[col]:     # Skip current position
                    nb = board.copy()     # Copy current board
                    nb[col] = row         # Move queen in this column
                    neighbors.append(nb)  # Store neighbor

        # Choose the neighbor with the minimum heuristic value
        next_board = min(neighbors, key=h)

        # If no improvement, we are at a local minimum
        if h(next_board) >= h(board):
            break                          # Stop search (failure case)

        # Move to the better neighbor
        board = next_board
        steps += 1

        # If solution found (no conflicts), stop
        if h(board) == 0:
            break

    # Return final board, final heuristic value, and steps taken
    return board, h(board), steps


# --------------------------------------------------
# Run the algorithm on 50 random initial boards
# --------------------------------------------------
results = []

for _ in range(50):
    # Generate random board
    # Each index = column, value = row
    board = [random.randint(0, 7) for _ in range(8)]

    initial_h = h(board)                  # Initial heuristic value

    # Apply hill climbing
    final_board, final_h, steps = steepest(board)

    # Check if solved
    status = "Solved" if final_h == 0 else "Fail"

    # Store results
    results.append((initial_h, final_h, steps, status, final_board))


# --------------------------------------------------
# Print results table
# --------------------------------------------------
print("InitH | FinalH | Steps | Status")
for r in results:
    print(f"{r[0]:>5} | {r[1]:>6} | {r[2]:>5} | {r[3]}")


# --------------------------------------------------
# Show an example of a local minimum (failure case)
# --------------------------------------------------
for r in results:
    if r[3] == "Fail":
        print("\nExample of Local Minimum:")
        print("Board:", r[4])
        print("Final h:", r[1])
        break