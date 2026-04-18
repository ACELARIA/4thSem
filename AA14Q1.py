def forward_chaining(facts, rules, goal):
    inferred = set(facts)
    step = 1

    print("\nInitial Facts:", inferred)

    while True:
        print(f"\n--- Step {step} ---")
        applied = False

        for condition, result in rules:
            print(f"Checking Rule: {condition} -> {result}")

            if all(c in inferred for c in condition):
                if result not in inferred:
                    print(f"Rule Applied: {condition} -> {result}")
                    inferred.add(result)
                    print("Updated Facts:", inferred)
                    applied = True

                    if result == goal:
                        print("\nGoal reached:", goal)
                        return True
                else:
                    print("Already inferred")
            else:
                print("Condition not satisfied")

        if not applied:
            print("\nNo more rules can be applied")
            break

        step += 1

    print("\nGoal NOT reached")
    return False


# -----------------------------
# Problem (a)
# -----------------------------
print("\n============================")
print("      Problem (a)")
print("============================")

facts_a = ['A', 'B', 'M']

rules_a = [
    (['P'], 'Q'),
    (['L', 'M'], 'P'),
    (['A', 'B'], 'L')
]

goal_a = 'Q'

forward_chaining(facts_a, rules_a, goal_a)


# -----------------------------
# Problem (b)
# -----------------------------
print("\n============================")
print("      Problem (b)")
print("============================")

facts_b = ['A', 'E']

rules_b = [
    (['A'], 'B'),
    (['B'], 'C'),
    (['C'], 'D'),
    (['D', 'E'], 'F')
]

goal_b = 'F'

forward_chaining(facts_b, rules_b, goal_b)