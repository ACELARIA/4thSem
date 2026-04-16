graph = {
    "Raj": ["Priya", "Sunil"],
    "Priya": ["Raj", "Aarav", "Aakash"],
    "Sunil": ["Raj", "Aakash", "Sneha"],
    "Aakash": ["Sunil", "Priya", "Neha"],
    "Neha": ["Aakash", "Aarav", "Rahul"],
    "Aarav": ["Priya", "Neha", "Arjun"],
    "Sneha": ["Sunil", "Rahul"],
    "Rahul": ["Neha", "Sneha", "Maya", "Pooja"],
    "Maya": ["Rahul", "Arjun"],
    "Arjun": ["Aarav", "Maya", "Pooja"],
    "Pooja": ["Rahul", "Arjun"]
}


def bfs_tree(graph, start):
    visited = set()
    queue = [start]
    tree = {}

    visited.add(start)

    while queue:
        node = queue.pop(0)
        tree[node] = []

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                tree[node].append(neighbor)

    return tree

def dfs_tree(graph, node, visited, tree):
    visited.add(node)
    tree[node] = []

    for neighbor in graph[node]:
        if neighbor not in visited:
            tree[node].append(neighbor)
            dfs_tree(graph, neighbor, visited, tree)

start_node = "Raj"

bfs_result = bfs_tree(graph, start_node)
print("BFS Tree:")
for parent in bfs_result:
    print(parent, "->", bfs_result[parent])

print("\nDFS Tree:")
dfs_result = {}
dfs_tree(graph, start_node, set(), dfs_result)
for parent in dfs_result:
    print(parent, "->", dfs_result[parent])
