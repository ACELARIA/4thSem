# -------------------------------------------------
# Possible boat moves
# (girls, boys)
# Boat can carry at most 2 people
# -------------------------------------------------
MOVES = [(1,0), (2,0), (0,1), (0,2), (1,1)]


# -------------------------------------------------
# Check whether a state is valid
# g = girls on left side
# b = boys on left side
# Rule: girls should never be outnumbered by boys on either side
# -------------------------------------------------
def valid(g, b):
    gr = 3 - g   # girls on right side
    br = 3 - b   # boys on right side

    # Conditions:
    # 1. Numbers must be between 0 and 3
    # 2. Girls must not be outnumbered by boys on left side
    # 3. Girls must not be outnumbered by boys on right side
    return (
        0 <= g <= 3 and
        0 <= b <= 3 and
        (g == 0 or g >= b) and
        (gr == 0 or gr >= br)
    )


# -------------------------------------------------
# Generate all valid next states
# state = (g, b, boat)
# boat = 0 → left side
# boat = 1 → right side
# -------------------------------------------------
def successors(state):
    g, b, boat = state
    next_states = []

    for dg, db in MOVES:
        if boat == 0:   # boat on left side
            ng = g - dg    # move girls to right
            nb = b - db    # move boys to right
            nb_side = 1    # boat now on right
        else:            # boat on right side
            ng = g + dg    # move girls back to left
            nb = b + db    # move boys back to left
            nb_side = 0    # boat now on left

        if valid(ng, nb):   # only add safe states
            next_states.append((ng, nb, nb_side))

    return next_states


# -------------------------------------------------
# Depth-Limited Search (DLS)
# state   → current state
# limit   → max depth allowed
# path    → path from start to current state
# explored→ visited states
# -------------------------------------------------
def dls(state, limit, path, explored):
    explored.add(state)   # mark visited

    # Goal: all girls and boys on right side, boat on right
    if state == (0, 0, 1):
        return path

    # Stop if depth limit reached
    if limit == 0:
        return "cutoff"

    cutoff_occurred = False

    # Expand next states
    for child in successors(state):
        if child not in explored:       # avoid revisiting
            result = dls(child, limit - 1, path + [child], explored)

            if result == "cutoff":
                cutoff_occurred = True
            elif result:                # solution found
                return result

    if cutoff_occurred:
        return "cutoff"
    else:
        return None


# -------------------------------------------------
# Run DLS with a fixed depth
# -------------------------------------------------
explored_dls = set()
result_dls = dls((3, 3, 0), 3, [(3, 3, 0)], explored_dls)

print("DLS Result:", result_dls)
print("DLS Explored States:", len(explored_dls))


# -------------------------------------------------
# Iterative Deepening Search (IDS)
# Repeatedly increases depth until solution is found
# -------------------------------------------------
def ids():
    depth = 0
    while True:
        explored = set()
        result = dls((3, 3, 0), depth, [(3, 3, 0)], explored)
        print("Depth:", depth, "Explored:", len(explored))

        if result and result != "cutoff":   # solution found
            return result, explored

        depth += 1


# -------------------------------------------------
# Run IDS and print solution path
# -------------------------------------------------
solution, explored_ids = ids()

print("\nIDS Solution Path:")
for step in solution:
    print(step)

print("IDS Explored States:", len(explored_ids))