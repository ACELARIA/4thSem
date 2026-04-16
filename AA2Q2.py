# -----------------------------
# 8-Puzzle using DFS
# -----------------------------

# Start state of the puzzle (0 represents blank)
start = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

# Goal state we want to reach
goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

# Possible movements of blank (row_change, column_change)
# Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# -------------------------------------------------
# Function to find the position of blank (0)
# -------------------------------------------------
def find_blank(state):
    for i in range(3):              # loop through rows
        for j in range(3):          # loop through columns
            if state[i][j] == 0:    # if blank found
                return i, j         # return its position


# -------------------------------------------------
# Function to generate all valid neighbor states
# -------------------------------------------------
def neighbors(state):

    x, y = find_blank(state)        # get blank position
    result = []                     # list to store next states

    for dx, dy in moves:            # try all 4 possible moves

        nx, ny = x + dx, y + dy     # new position of blank

        # check if new position is inside 3x3 grid
        if 0 <= nx < 3 and 0 <= ny < 3:

            # convert tuple to list so we can modify it
            board = [list(row) for row in state]

            # swap blank with adjacent tile
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

            # convert list back to tuple (so it can be stored in set)
            new_state = tuple(tuple(row) for row in board)

            result.append(new_state)   # add new state to list

    return result                      # return all possible next states


# -------------------------------------------------
# Depth First Search (DFS)
# -------------------------------------------------

# Stack stores (state, depth)
# Depth = number of moves taken
stack = [(start, 0)]

# Visited set to avoid revisiting same states
visited = set([start])

# Counter to track how many states were explored
explored = 0


# Run DFS until stack becomes empty
while stack:

    # Remove last element (LIFO → DFS behavior)
    state, depth = stack.pop()

    explored += 1   # increase explored counter

    # Check if goal reached
    if state == goal:
        print("DFS Goal Depth =", depth)
        print("DFS States Explored =", explored)
        break

    # Generate all neighbor states
    for n in neighbors(state):

        # If not already visited
        if n not in visited:
            visited.add(n)                 # mark as visited
            stack.append((n, depth + 1))   # push to stack with depth+1