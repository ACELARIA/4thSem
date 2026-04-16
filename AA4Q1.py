adj = {
    "Portland": [("Boston", 107)],
    "Boston": [("Syracuse", 312), ("New York", 215), ("Providence", 50)],
    "Providence": [("Boston", 50), ("New York", 181)],
    "New York": [("Syracuse", 254), ("Boston", 215), ("Philadelphia", 97), ("Providence", 181)],
    "Syracuse": [("Buffalo", 150), ("Philadelphia", 253), ("Boston", 312), ("New York", 254)],
    "Philadelphia": [("Pittsburgh", 305), ("Baltimore", 101), ("New York", 97), ("Syracuse", 253)],
    "Baltimore": [("Philadelphia", 101), ("Pittsburgh", 247)],
    "Buffalo": [("Syracuse", 150), ("Detroit", 256), ("Cleveland", 189), ("Pittsburgh", 215)],
    "Pittsburgh": [("Cleveland", 134), ("Columbus", 185), ("Philadelphia", 305), ("Baltimore", 247), ("Buffalo", 215)],
    "Detroit": [("Buffalo", 256), ("Cleveland", 169), ("Chicago", 283)],
    "Cleveland": [("Buffalo", 189), ("Detroit", 169), ("Chicago", 345), ("Columbus", 144), ("Pittsburgh", 134)],
    "Columbus": [("Cleveland", 144), ("Pittsburgh", 185), ("Indianapolis", 176)],
    "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
    "Indianapolis": [("Columbus", 176), ("Chicago", 182)],
}

# --------------------------------
# BEST-FIRST / UNIFORM COST SEARCH
# --------------------------------
def best_first_search(start, goal):

    # frontier stores tuples of:
    # (total_cost_so_far, current_city, path_taken)
    frontier = [(0, start, [start])]

    # visited set prevents revisiting cities
    visited = set()

    # counter to track how many nodes were explored
    explored_count = 0

    # Continue searching while there are paths in frontier
    while frontier:

        # Sort frontier so smallest cost is first
        frontier.sort()

        # Remove and get the path with lowest cost
        cost, city, path = frontier.pop(0)

        # Increase explored counter
        explored_count += 1

        # If goal reached, return results
        if city == goal:
            return path, cost, explored_count

        # Skip if city already visited
        if city in visited:
            continue

        # Mark current city as visited
        visited.add(city)

        # Expand all neighboring cities
        for next_city, distance in adj.get(city, []):

            # Only consider unvisited cities
            if next_city not in visited:

                # Add new path to frontier
                # New cost = current cost + distance
                # New path = old path + next city
                frontier.append(
                    (cost + distance, next_city, path + [next_city])
                )

    # If no path found
    return None, None, explored_count


# -------------------------------
# DRIVER CODE
# -------------------------------

# Define start and goal cities
start = "Syracuse"
goal = "Chicago"

# Call the search function
path, total_cost, count = best_first_search(start, goal)

# Print results
if path:
    print("Path:", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found")

print("Paths explored:", count)