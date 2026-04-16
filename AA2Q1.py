# -------------------------------
# 8-Puzzle using Breadth-First Search (BFS)
# -------------------------------

# Initial board configuration (0 = blank space)
start = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

# Goal board configuration
goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

# Possible movements of blank tile:
# (-1,0) = up
# (1,0)  = down
# (0,-1) = left
# (0,1)  = right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Function to find position of blank tile (0)
def find_blank(state):
    for i in range(3):          # Loop through rows
        for j in range(3):      # Loop through columns
            if state[i][j] == 0:  # If blank tile found
                return i, j     # Return its position


# Function to generate all valid next states
def neighbors(state):
    x, y = find_blank(state)    # Get blank position
    result = []                 # Store neighboring states

    for dx, dy in moves:        # Try all 4 directions
        nx, ny = x + dx, y + dy  # New position after move

        # Check if new position is inside board
        if 0 <= nx < 3 and 0 <= ny < 3:

            # Convert tuple to list so we can modify it
            board = [list(row) for row in state]

            # Swap blank tile with adjacent tile
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

            # Convert back to tuple (so it can be stored in set)
            new_state = tuple(tuple(row) for row in board)

            # Add new state to result list
            result.append(new_state)

    return result   # Return all valid neighboring states


# -------------------------------
# BFS Algorithm
# -------------------------------

queue = [(start, 0)]     # Queue stores (state, depth)
visited = set([start])   # Keep track of visited states
explored = 0             # Count how many states explored

while queue:

    # Remove first element (FIFO -> BFS behavior)
    state, depth = queue.pop(0)
    explored += 1

    # If goal state is reached
    if state == goal:
        print("Goal Depth =", depth)          # Number of moves required
        print("States Explored =", explored)  # Total states checked
        break

    # Generate all next possible states
    for n in neighbors(state):

        # If state not visited before
        if n not in visited:
            visited.add(n)                # Mark as visited
            queue.append((n, depth + 1))  # Add to queue with increased depth