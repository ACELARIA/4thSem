from collections import deque

# -----------------------------
# Input Sudoku (0 = empty)
# -----------------------------
grid = [
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,0,8,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,0,7,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,2]
]

# -----------------------------
# Variables and Domains
# -----------------------------
cells = [(r, c) for r in range(9) for c in range(9)]

domains = {}
for r in range(9):
    for c in range(9):
        if grid[r][c] == 0:
            domains[(r,c)] = list(range(1,10))
        else:
            domains[(r,c)] = [grid[r][c]]

# -----------------------------
# Get neighbors (row, col, box)
# -----------------------------
def get_neighbors(r, c):
    neighbors = set()

    # Row & Column
    for i in range(9):
        if i != c:
            neighbors.add((r, i))
        if i != r:
            neighbors.add((i, c))

    # 3x3 box
    br, bc = (r//3)*3, (c//3)*3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if (i, j) != (r, c):
                neighbors.add((i, j))

    return neighbors

# -----------------------------
# Generate all arcs
# -----------------------------
arcs = []
for cell in cells:
    for neighbor in get_neighbors(*cell):
        arcs.append((cell, neighbor))

print("Total arcs generated:", len(arcs))  # ~1620 directed arcs


# -----------------------------
# Constraint: Xi != Xj
# -----------------------------
def constraint(x, y):
    return x != y


# -----------------------------
# REVISE
# -----------------------------
def revise(domains, Xi, Xj):
    revised = False
    to_remove = []

    for x in domains[Xi]:
        if not any(constraint(x, y) for y in domains[Xj]):
            to_remove.append(x)

    for x in to_remove:
        domains[Xi].remove(x)
        revised = True

    return revised, len(to_remove)


# -----------------------------
# AC-3
# -----------------------------
def ac3(domains):
    queue = deque(arcs)
    total_removed = 0

    while queue:
        Xi, Xj = queue.popleft()

        revised, removed_count = revise(domains, Xi, Xj)
        total_removed += removed_count

        if revised:
            if len(domains[Xi]) == 0:
                return False, total_removed

            for Xk in get_neighbors(*Xi):
                if Xk != Xj:
                    queue.append((Xk, Xi))

    return True, total_removed


# -----------------------------
# Run AC-3
# -----------------------------
result, removed_values = ac3(domains)

print("\nArc Consistent:", result)
print("Total values removed:", removed_values)


# -----------------------------
# Visualization (domain sizes)
# -----------------------------
print("\nDomain size grid:\n")
for r in range(9):
    row = []
    for c in range(9):
        row.append(str(len(domains[(r,c)])))
    print(" ".join(row))