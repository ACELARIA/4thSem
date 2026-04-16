from collections import deque

# -----------------------------
# Variables and Domains
# -----------------------------
variables = ["P1", "P2", "P3", "P4", "P5", "P6"]

domains = {
    v: ["R1", "R2", "R3"] for v in variables
}

# -----------------------------
# Constraints (neighbors)
# -----------------------------
neighbors = {
    "P1": ["P2", "P3", "P6"],
    "P2": ["P1", "P3", "P4"],
    "P3": ["P1", "P2", "P5"],
    "P4": ["P2", "P6"],
    "P5": ["P3", "P6"],
    "P6": ["P1", "P4", "P5"]
}

# Constraint: Xi != Xj
def constraint(x, y):
    return x != y


# -----------------------------
# REVISE function
# -----------------------------
def revise(domains, Xi, Xj):
    revised = False
    to_remove = []

    for x in domains[Xi]:
        # Check if there is NO supporting value in Xj
        if not any(constraint(x, y) for y in domains[Xj]):
            to_remove.append(x)

    for x in to_remove:
        domains[Xi].remove(x)
        revised = True

    return revised


# -----------------------------
# AC-3 Algorithm
# -----------------------------
def ac3(domains, trace_limit=5):
    queue = deque()

    # Initialize all arcs
    for Xi in variables:
        for Xj in neighbors[Xi]:
            queue.append((Xi, Xj))

    step = 0

    while queue:
        Xi, Xj = queue.popleft()

        changed = revise(domains, Xi, Xj)

        # Trace first few steps
        if step < trace_limit:
            if changed:
                print(f"Arc ({Xi},{Xj}) checked → domain reduced: {domains[Xi]}")
            else:
                print(f"Arc ({Xi},{Xj}) checked → no change")
            step += 1

        if changed:
            if not domains[Xi]:
                return False  # Failure (empty domain)

            for Xk in neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))

    return True


# -----------------------------
# RUN WITHOUT ASSIGNMENT
# -----------------------------
print("=== AC-3 without assignment ===")
domains_copy = {v: domains[v][:] for v in variables}

result = ac3(domains_copy)

print("\nArc Consistent:", result)
print("Domains:", domains_copy)


# -----------------------------
# RUN WITH P1 = R1
# -----------------------------
print("\n=== AC-3 with P1 = R1 ===")
domains_copy = {v: domains[v][:] for v in variables}

# Assign P1 = R1
domains_copy["P1"] = ["R1"]

result = ac3(domains_copy)

print("\nArc Consistent after assignment:", result)
print("Domains:", domains_copy)