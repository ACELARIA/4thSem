from itertools import product

# -----------------------------
# Symbol Class
# -----------------------------
class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


# -----------------------------
# Logical Operations
# -----------------------------
def NOT(p):
    return not p

def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def IMPLIES(p, q):   # p -> q
    return (not p) or q

def IFF(p, q):       # p <-> q
    return p == q


# -----------------------------
# Truth Table Printer
# -----------------------------
def print_truth_table(expr_func, variables, title):
    print(f"\nTruth Table for: {title}")
    print("-" * 50)

    # Header
    for var in variables:
        print(var, end="\t")
    print("Result")

    # Generate combinations
    for values in product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))
        result = expr_func(**env)

        for v in values:
            print('T' if v else 'F', end="\t")
        print('T' if result else 'F')


# -----------------------------
# Propositions
# -----------------------------

# 1. ~P -> Q
f1 = lambda P, Q: IMPLIES(NOT(P), Q)

# 2. ~P ∧ ~Q
f2 = lambda P, Q: AND(NOT(P), NOT(Q))

# 3. ~P ∨ ~Q
f3 = lambda P, Q: OR(NOT(P), NOT(Q))

# 4. ~P -> ~Q
f4 = lambda P, Q: IMPLIES(NOT(P), NOT(Q))

# 5. ~P <-> ~Q
f5 = lambda P, Q: IFF(NOT(P), NOT(Q))

# 6. (P ∨ Q) ∧ (~P -> Q)
f6 = lambda P, Q: AND(OR(P, Q), IMPLIES(NOT(P), Q))

# 7. (P ∨ Q) -> ~R
f7 = lambda P, Q, R: IMPLIES(OR(P, Q), NOT(R))

# 8. ((P ∨ Q)->~R) <-> ((~P∧~Q)->~R)
f8 = lambda P, Q, R: IFF(
    IMPLIES(OR(P, Q), NOT(R)),
    IMPLIES(AND(NOT(P), NOT(Q)), NOT(R))
)

# 9. ((P->Q) ∧ (Q->R)) -> (Q->R)
f9 = lambda P, Q, R: IMPLIES(
    AND(IMPLIES(P, Q), IMPLIES(Q, R)),
    IMPLIES(Q, R)
)

# 10. ((P->(Q∨R)) -> (~P∧~Q∧~R))
f10 = lambda P, Q, R: IMPLIES(
    IMPLIES(P, OR(Q, R)),
    AND(NOT(P), AND(NOT(Q), NOT(R)))
)


# -----------------------------
# Run All Truth Tables
# -----------------------------
print_truth_table(f1, ['P', 'Q'], "~P -> Q")
print_truth_table(f2, ['P', 'Q'], "~P ∧ ~Q")
print_truth_table(f3, ['P', 'Q'], "~P ∨ ~Q")
print_truth_table(f4, ['P', 'Q'], "~P -> ~Q")
print_truth_table(f5, ['P', 'Q'], "~P <-> ~Q")
print_truth_table(f6, ['P', 'Q'], "(P ∨ Q) ∧ (~P -> Q)")

print_truth_table(f7, ['P', 'Q', 'R'], "(P ∨ Q) -> ~R")
print_truth_table(f8, ['P', 'Q', 'R'], "((P ∨ Q)->~R) <-> ((~P∧~Q)->~R)")
print_truth_table(f9, ['P', 'Q', 'R'], "((P->Q)∧(Q->R))->(Q->R)")
print_truth_table(f10, ['P', 'Q', 'R'], "((P->(Q∨R)) -> (~P∧~Q∧~R))")