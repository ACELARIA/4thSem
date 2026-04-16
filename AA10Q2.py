# States: (Location, A, B)
# Location: 'A' or 'B'
# Tile state: 'D' (Dirty), 'C' (Clean)

iteration = 0  # global counter


def goal_test(state):
    return state[1] == 'C' and state[2] == 'C'


# Possible nondeterministic results of actions
def results(state, action):
    loc, A, B = state

    if action == "SUCK":
        if loc == 'A':
            if A == 'D':
                return [
                    ('A', 'C', B),
                    ('A', 'C', 'C')
                ]
            else:
                return [
                    ('A', 'C', B),
                    ('A', 'D', B)
                ]

        if loc == 'B':
            if B == 'D':
                return [
                    ('B', A, 'C'),
                    ('B', 'C', 'C')
                ]
            else:
                return [
                    ('B', A, 'C'),
                    ('B', A, 'D')
                ]

    elif action == "RIGHT":
        return [('B', A, B)]

    elif action == "LEFT":
        return [('A', A, B)]

    return []


# AND-OR Graph Search
def and_or_search(state):
    return or_search(state, [])


def or_search(state, path):
    global iteration
    iteration += 1

    print(f"\n[Iteration {iteration}] OR-Search at state: {state}")
    print(f"Path: {path}")

    if goal_test(state):
        print("Goal reached!")
        return "GOAL"

    if state in path:
        print("Loop detected. Backtracking...")
        return None

    for action in ["SUCK", "RIGHT", "LEFT"]:
        print(f"Trying action: {action}")

        result_states = results(state, action)
        print(f"Possible outcomes: {result_states}")

        plan = and_search(result_states, path + [state])

        if plan is not None:
            print(f"Action {action} leads to a valid plan")
            return {action: plan}

    print("All actions failed. Backtracking...")
    return None


def and_search(states, path):
    global iteration
    iteration += 1

    print(f"\n[Iteration {iteration}] AND-Search on states: {states}")

    plans = {}

    for s in states:
        print(f"Exploring state: {s}")
        plan = or_search(s, path)

        if plan is None:
            print(f"State {s} failed. AND condition fails.")
            return None

        plans[s] = plan

    print("All states succeeded in AND-search")
    return plans


# -----------------------------
# Run the Agent
# -----------------------------
initial_state = ('A', 'D', 'D')

solution = and_or_search(initial_state)

print("\nFinal AND-OR Plan:\n")
print(solution)