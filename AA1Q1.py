graph = {
    "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
    "Detroit": [("Chicago", 283), ("Cleveland", 169), ("Buffalo", 256)],
    "Cleveland": [("Chicago", 345), ("Detroit", 169), ("Columbus", 144), ("Pittsburgh", 134)],
    "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
    "Columbus": [("Indianapolis", 176), ("Cleveland", 144), ("Pittsburgh", 185)],
    "Pittsburgh": [("Cleveland", 134), ("Columbus", 185), ("Buffalo", 215),
                    ("Syracuse", 253), ("Baltimore", 247), ("Philadelphia", 305)],
    "Buffalo": [("Detroit", 256), ("Pittsburgh", 215), ("Syracuse", 150)],
    "Syracuse": [("Buffalo", 150), ("Pittsburgh", 253), ("Boston", 312)],
    "Baltimore": [("Pittsburgh", 247), ("Philadelphia", 101)],
    "Philadelphia": [("Baltimore", 101), ("Pittsburgh", 305), ("New York", 97)],
    "New York": [("Philadelphia", 97), ("Boston", 215)],
    "Boston": [("New York", 215), ("Providence", 50), ("Portland", 107)],
    "Providence": [("Boston", 50)],
    "Portland": [("Boston", 107)]
}

def bfs_all_paths(graph, start, goal):
    queue = [(start, [start], 0)]  
    paths = []

    while queue:
        current, path, cost = queue.pop(0)

        if current == goal:
            paths.append((path, cost))
            continue

        for neighbor, weight in graph[current]:
            if neighbor not in path:   
                queue.append((neighbor, path + [neighbor], cost + weight))

    return paths

def dfs_all_paths(graph, current, goal, path, cost, paths):
    if current == goal:
        paths.append((path, cost))
        return

    for neighbor, weight in graph[current]:
        if neighbor not in path:
            dfs_all_paths(graph, neighbor, goal,path + [neighbor], cost + weight, paths)

def dfs_wrapper(graph, start, goal):
    paths = []
    dfs_all_paths(graph, start, goal, [start], 0, paths)
    return paths


start = "Syracuse"
goal = "Chicago"

print("BFS Paths:\n")
bfs_paths = bfs_all_paths(graph, start, goal)
for p, c in bfs_paths:
    print(" -> ".join(p), " | Cost =", c)

print("\nDFS Paths:\n")
dfs_paths = []
dfs_paths = dfs_wrapper(graph, start, goal)
for p, c in dfs_paths:
    print(" -> ".join(p), " | Cost =", c)
