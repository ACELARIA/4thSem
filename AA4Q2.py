# Heuristic function (Manhattan Distance)
def h(a, b):
    # a and b are coordinates like (row, col)
    # abs difference in rows + abs difference in columns
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Greedy Best-First Search function
def bestfs(grid, start, goal):

    # OPEN list → stores nodes to be explored
    open_list = [start]

    # VISITED list → stores already explored nodes
    visited = []

    # PARENT dictionary → used to reconstruct path
    parent = {}

    # Run until there are no nodes left to explore
    while open_list:

        # Assume first node is the best
        curr = open_list[0]

        # Find node in open_list with smallest heuristic value
        for n in open_list:
            if h(n, goal) < h(curr, goal):
                curr = n

        # Remove selected node from open_list
        open_list.remove(curr)

        # Mark it as visited
        visited.append(curr)

        # If goal is reached → reconstruct path
        if curr == goal:
            path = []

            # Backtrack from goal to start using parent dictionary
            while curr in parent:
                path.append(curr)
                curr = parent[curr]

            # Add start node
            path.append(start)

            # Reverse because we built path from goal → start
            path.reverse()

            return path

        # Get current row and column
        x, y = curr

        # Possible 4 movements (Up, Down, Left, Right)
        neighbors = [
            (x - 1, y),  # Up
            (x + 1, y),  # Down
            (x, y - 1),  # Left
            (x, y + 1)   # Right
        ]

        # Check each neighbor
        for m in neighbors:
            r, c = m

            # Check if inside grid boundaries
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):

                # Check if cell is free (0) and not visited
                if grid[r][c] == 0 and m not in visited:

                    # Add to open_list for future exploration
                    open_list.append(m)

                    # Store parent for path reconstruction
                    parent[m] = curr

    # If goal is not reachable
    return None


# ------------------ GRID ------------------
# 0 = free path
# 1 = wall

grid = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],   # horizontal hallway
    [1,1,0,1,1],
    [1,1,0,1,1]
]

# Start position (row 4, column 2)
start = (4,2)

# Goal position (row 2, column 4)
goal = (2,4)

# Print result
print("Evacuation Path:")
print(bestfs(grid, start, goal))