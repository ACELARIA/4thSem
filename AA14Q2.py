def backward_chaining(goal, facts, rules, visited, depth=0):
    indent = "  " * depth
    print(f"{indent}Goal: {goal}")

    # If already a known fact
    if goal in facts:
        print(f"{indent}{goal} is a FACT")
        return True

    # Avoid loops
    if goal in visited:
        print(f"{indent}Already visited {goal}, avoid loop")
        return False

    visited.add(goal)

    # Find rules that conclude this goal
    applicable_rules = [r for r in rules if r[1] == goal]

    if not applicable_rules:
        print(f"{indent}No rule found for {goal}")
        return False

    # Try each rule
    for condition, result in applicable_rules:
        print(f"{indent}Trying Rule: {condition} -> {result}")

        all_true = True
        for subgoal in condition:
            if not backward_chaining(subgoal, facts, rules, visited, depth + 1):
                all_true = False
                break

        if all_true:
            print(f"{indent}Rule satisfied for {goal}")
            facts.add(goal)  # add inferred fact
            return True

    print(f"{indent}Cannot prove {goal}")
    return False


# -----------------------------
# Problem (a)
# -----------------------------
print("\n============================")
print("      Problem (a)")
print("============================")

facts_a = set(['A', 'B'])

rules_a = [
    (['P'], 'Q'),
    (['R'], 'Q'),
    (['A'], 'P'),
    (['B'], 'R')
]

goal_a = 'Q'

if backward_chaining(goal_a, facts_a, rules_a, set()):
    print("\nGoal Q reached")
else:
    print("\nGoal Q NOT reached")


# -----------------------------
# Problem (b)
# -----------------------------
print("\n============================")
print("      Problem (b)")
print("============================")

facts_b = set(['A', 'E'])

rules_b = [
    (['A'], 'B'),
    (['B', 'C'], 'D'),
    (['E'], 'C')
]

goal_b = 'D'

if backward_chaining(goal_b, facts_b, rules_b, set()):
    print("\nGoal D reached")
else:
    print("\nGoal D NOT reached")