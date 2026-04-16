import heapq   # Used to implement priority queue (min-heap) for A* search

# -------------------------------------------------
# 5x5 Grid Representation
# 0 = Empty cell
# 1 = Wall (Blocked)
# 2 = Start position
# 3 = Reward / Goal
# -------------------------------------------------
grid = [
    [2, 0, 0, 0, 3],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [3, 0, 1, 0, 3]
]

ROWS = 5   # Total rows in grid
COLS = 5   # Total columns in grid


# -------------------------------------------------
# Function to find start and all reward positions
# -------------------------------------------------
def find_positions(grid):
    start = None        # Will store start position
    rewards = []        # Will store all goal positions

    # Scan entire grid
    for r in range(ROWS):
        for c in range(COLS):

            # If cell contains 2 → it is start
            if grid[r][c] == 2:
                start = (r, c)

            # If cell contains 3 → it is a reward
            elif grid[r][c] == 3:
                rewards.append((r, c))

    # Return start and list of rewards
    return start, rewards


# -------------------------------------------------
# Manhattan Distance Heuristic
# Formula: |x1 - x2| + |y1 - y2|
# Used because movement is only up/down/left/right
# -------------------------------------------------
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -------------------------------------------------
# Multi-Goal Heuristic Function
# Returns distance to the nearest remaining goal
# -------------------------------------------------
def heuristic(position, remaining_goals):

    # If no goals remain, cost is 0 (search complete)
    if not remaining_goals:
        return 0

    # Compute Manhattan distance to each remaining goal
    # Return minimum (nearest goal)
    return min(manhattan(position, goal) for goal in remaining_goals)


# -------------------------------------------------
# Get all valid neighboring cells
# -------------------------------------------------
def get_neighbors(position):

    r, c = position

    # Possible movements → Right, Left, Down, Up
    moves = [(0,1), (0,-1), (1,0), (-1,0)]

    neighbors = []

    for dr, dc in moves:
        nr = r + dr
        nc = c + dc

        # Check boundaries of grid
        if 0 <= nr < ROWS and 0 <= nc < COLS:

            # Check if not a wall
            if grid[nr][nc] != 1:
                neighbors.append((nr, nc))

    return neighbors


# -------------------------------------------------
# Multi-Goal A* Search Algorithm
# -------------------------------------------------
def multi_goal_astar(grid):

    # Get start and goal positions
    start, goals = find_positions(grid)

    open_list = []  # Priority queue (min-heap)

    # Convert goals list to tuple (so it can be stored in set)
    initial_remaining = tuple(goals)

    # Push start node into priority queue
    # Format: (f, g, current_position, remaining_goals, path)
    heapq.heappush(
        open_list,
        (
            heuristic(start, goals),  # f = h (since g = 0 initially)
            0,                        # g = 0 (cost so far)
            start,                    # current position
            initial_remaining,        # goals not yet visited
            [start]                   # path so far
        )
    )

    visited_states = set()  # To avoid revisiting same state
    expanded_nodes = []     # To track search effort

    # Main A* Loop
    while open_list:

        # Pop node with smallest f value
        f, g, current, remaining, path = heapq.heappop(open_list)

        # State includes position AND remaining goals
        state = (current, remaining)

        # Skip if already visited
        if state in visited_states:
            continue

        visited_states.add(state)
        expanded_nodes.append(current)

        # Convert tuple to list so we can modify it
        remaining_goals = list(remaining)

        # If current cell is a goal → remove it
        if current in remaining_goals:
            remaining_goals.remove(current)

        # If no goals remain → solution found
        if not remaining_goals:
            return path, expanded_nodes

        # Expand neighbors
        for neighbor in get_neighbors(current):

            new_g = g + 1   # Cost of moving (each step = 1)

            new_remaining = tuple(remaining_goals)

            # f = g + h
            new_f = new_g + heuristic(neighbor, new_remaining)

            # Push new state into priority queue
            heapq.heappush(
                open_list,
                (
                    new_f,
                    new_g,
                    neighbor,
                    new_remaining,
                    path + [neighbor]
                )
            )

    # If no solution found
    return None, expanded_nodes


# -------------------------------------------------
# Run the Algorithm
# -------------------------------------------------
path, visited = multi_goal_astar(grid)

print("========== FINAL RESULT ==========")

# If path found
if path:
    print("\nSolution Path:")
    print(path)

    print("\nTotal Moves (Steps):", len(path) - 1)
else:
    print("No solution found.")

print("\nTiles Expanded (Search Effort):")
print(visited)

print("\nTotal Nodes Expanded:", len(visited))