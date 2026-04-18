def negate_literal(lit):
    return lit[1:] if lit.startswith('¬') else '¬' + lit


def resolve(ci, cj):
    resolvents = []
    for di in ci:
        for dj in cj:
            if di == negate_literal(dj):
                new_clause = (ci - {di}) | (cj - {dj})
                resolvents.append(new_clause)
    return resolvents


def resolution(kb, query):
    # Add negation of query
    clauses = kb.copy()
    clauses.append({negate_literal(query)})

    print("\nInitial Clauses:")
    for c in clauses:
        print(c)

    new = []
    step = 1

    while True:
        print(f"\n--- Step {step} ---")
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]

        for (ci, cj) in pairs:
            print(f"Resolving {ci} and {cj}")
            resolvents = resolve(ci, cj)

            for r in resolvents:
                print("→ Derived:", r)
                if not r:  # empty clause
                    print("\nEmpty clause found → PROVED")
                    return True
                if r not in clauses and r not in new:
                    new.append(r)

        if all(r in clauses for r in new):
            print("\nNo new clauses → NOT PROVED")
            return False

        clauses.extend(new)
        step += 1


# -----------------------------
# Problem (a)
# -----------------------------
print("\n============================")
print("      Problem (a)")
print("============================")

# CNF Conversion:
# P ∨ Q → {P, Q}
# P → R → ¬P ∨ R → {¬P, R}
# Q → S → ¬Q ∨ S → {¬Q, S}
# R → S → ¬R ∨ S → {¬R, S}

kb_a = [
    {'P', 'Q'},
    {'¬P', 'R'},
    {'¬Q', 'S'},
    {'¬R', 'S'}
]

query_a = 'S'

resolution(kb_a, query_a)


# -----------------------------
# Problem (b)
# -----------------------------
print("\n============================")
print("      Problem (b)")
print("============================")

# CNF Conversion:
# P → Q → ¬P ∨ Q → {¬P, Q}
# Q → R → ¬Q ∨ R → {¬Q, R}
# S → ¬R → ¬S ∨ ¬R → {¬S, ¬R}
# P → {P}

kb_b = [
    {'¬P', 'Q'},
    {'¬Q', 'R'},
    {'¬S', '¬R'},
    {'P'}
]

query_b = 'S'

resolution(kb_b, query_b)