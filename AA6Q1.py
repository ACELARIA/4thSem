import heapq   # Used to create a priority queue (min-heap)

# ---------------- HEURISTIC VALUES ----------------
# Estimated distance from each city to Boston (goal)
# h(n) values
heuristic = {
    "Boston": 0,          # Goal has heuristic 0
    "Providence": 50,
    "Portland": 107,
    "New York": 215,
    "Philadelphia": 270,
    "Baltimore": 360,
    "Syracuse": 260,
    "Buffalo": 400,
    "Pittsburgh": 470,
    "Cleveland": 550,
    "Columbus": 640,
    "Detroit": 610,
    "Indianapolis": 780,
    "Chicago": 860
}

# ---------------- GRAPH ----------------
# Graph represented as adjacency list
# Each city connects to neighbors with actual travel cost
graph = {
    "Chicago": {"Detroit": 280, "Indianapolis": 180},
    "Detroit": {"Chicago": 280, "Cleveland": 170},
    "Indianapolis": {"Chicago": 180, "Columbus": 175},
    "Columbus": {"Indianapolis": 175, "Pittsburgh": 185},
    "Cleveland": {"Detroit": 170, "Pittsburgh": 135, "Buffalo": 190},
    "Pittsburgh": {"Columbus": 185, "Cleveland": 135, "Philadelphia": 305},
    "Buffalo": {"Cleveland": 190, "Syracuse": 150},
    "Syracuse": {"Buffalo": 150, "New York": 250},
    "Philadelphia": {"Pittsburgh": 305, "New York": 95, "Baltimore": 100},
    "Baltimore": {"Philadelphia": 100},
    "New York": {"Philadelphia": 95, "Syracuse": 250, "Providence": 155},
    "Providence": {"New York": 155, "Boston": 50},
    "Portland": {"Boston": 110},
    "Boston": {}
}

# ---------------- GREEDY BEST-FIRST SEARCH ----------------
def greedy_best_first(graph, heuristic, start, goal):

    open_list = []   # Priority queue (min-heap)
    
    # Insert start node with its heuristic value
    # Format: (priority, node)
    heapq.heappush(open_list, (heuristic[start], start))

    visited = set()   # Keeps track of explored nodes
    parent = {}       # Stores path (child -> parent)
    explored_count = 0

    # Continue until there are nodes to explore
    while open_list:

        # Remove node with smallest heuristic value
        _, current = heapq.heappop(open_list)

        # Skip if already visited
        if current in visited:
            continue

        visited.add(current)  # Mark node as visited
        explored_count += 1

        # Stop if goal reached
        if current == goal:
            break

        # Explore neighbors
        for neighbor in graph[current]:

            if neighbor not in visited:
                # Greedy uses ONLY heuristic value
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                
                # Store parent to reconstruct path later
                parent[neighbor] = current

    # -------- Path Reconstruction --------
    path = []
    node = goal

    # Move backwards from goal to start
    while node != start:
        path.append(node)
        node = parent.get(node, start)

        if node == start:
            path.append(start)
            break

    path.reverse()  # Reverse to get start -> goal
    return path, explored_count


# ---------------- A* SEARCH ----------------
def a_star(graph, heuristic, start, goal):

    open_list = []

    # Insert start node
    # Format: (f(n), g(n), node)
    # f(n) = g(n) + h(n)
    heapq.heappush(open_list, (heuristic[start], 0, start))

    g_cost = {start: 0}   # Stores shortest known cost from start
    parent = {}
    visited = set()
    explored_count = 0

    while open_list:

        # Pop node with smallest f(n)
        _, current_g, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)
        explored_count += 1

        if current == goal:
            break

        # Explore neighbors with actual cost
        for neighbor, cost in graph[current].items():

            # Calculate new actual cost from start
            new_g = current_g + cost

            # Update if new path is shorter
            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g

                # Calculate f(n) = g(n) + h(n)
                f_cost = new_g + heuristic[neighbor]

                # Push into priority queue
                heapq.heappush(open_list, (f_cost, new_g, neighbor))

                parent[neighbor] = current

    # -------- Path Reconstruction --------
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent.get(node, start)

        if node == start:
            path.append(start)
            break

    path.reverse()
    return path, explored_count


# ---------------- RUN BOTH ALGORITHMS ----------------

start = "Chicago"
goal = "Boston"

# Run Greedy Search
greedy_path, greedy_explored = greedy_best_first(graph, heuristic, start, goal)

# Run A* Search
astar_path, astar_explored = a_star(graph, heuristic, start, goal)

# Print Results
print("Greedy Path:", greedy_path)
print("Greedy Nodes Explored:", greedy_explored)

print("A* Path:", astar_path)
print("A* Nodes Explored:", astar_explored)