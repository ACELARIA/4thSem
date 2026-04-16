EMPTY, X, O = " ", "X", "O"

nodes = 0
call_count = 0

def create_board():
    return [EMPTY] * 9


def print_board(b):
    print("\n     0   1   2\n   -----------")
    for i in range(3):
        r = i * 3
        print(f" {i} | {b[r]} | {b[r+1]} | {b[r+2]} |")
        print("   -----------")
    print()


def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for a,b1,c in wins:
        if b[a] == b[b1] == b[c] != EMPTY:
            return b[a]
    return None


def terminal(b):
    return winner(b) is not None or EMPTY not in b


def utility(b):
    w = winner(b)
    return 1 if w == X else -1 if w == O else 0


def actions(b):
    return [i for i in range(9) if b[i] == EMPTY]


def result(b, move, player):
    new = b.copy()
    new[move] = player
    return new


def max_value(b):
    global nodes, call_count
    nodes += 1
    call_count += 1

    if terminal(b):
        return utility(b), None

    best_val, best_move = -999, None

    for m in actions(b):
        val, _ = min_value(result(b, m, X))
        if val > best_val:
            best_val, best_move = val, m

    return best_val, best_move


def min_value(b):
    global nodes, call_count
    nodes += 1
    call_count += 1

    if terminal(b):
        return utility(b), None

    best_val, best_move = 999, None

    for m in actions(b):
        val, _ = max_value(result(b, m, O))
        if val < best_val:
            best_val, best_move = val, m

    return best_val, best_move


def minimax(b):
    return max_value(b)[1], max_value(b)[0]


def print_tree_simple(b, depth=0, player=X, max_depth=3):
    if terminal(b) or depth >= max_depth:
        print("  " * depth + f"→ Value: {utility(b)}")
        return

    moves = actions(b)

    for i, m in enumerate(moves):
        prefix = "└──" if i == len(moves) - 1 else "├──"

        if player == X:
            val, _ = min_value(result(b, m, player))
            label = "MAX (X)"
        else:
            val, _ = max_value(result(b, m, player))
            label = "MIN (O)"

        print("  " * depth + f"{prefix} {label} plays {m} → Value {val}")

        next_p = O if player == X else X
        print_tree_simple(result(b, m, player), depth + 1, next_p, max_depth)


def print_game_stats():
    print("\n" + "="*50)
    print("MINIMAX ALGORITHM PERFORMANCE STATISTICS")
    print("="*50)
    print(f"Total nodes explored: {nodes}")
    print(f"Total function calls: {call_count}")
    if call_count:
        print(f"Nodes per call: {nodes/call_count:.2f}")
    print("="*50 + "\n")


# MAIN
print("\n" + "="*50)
print("TIC-TAC-TOE WITH MINIMAX ALGORITHM")
print("="*50)
print("YOU are O | AI is X\n")

board = create_board()
move_count = 0

while not terminal(board):
    print_board(board)

    # Player move
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in range(9) and board[move] == EMPTY:
                break
            print("Invalid move!")
        except:
            print("Enter a number!")

    board[move] = O
    move_count += 1

    if terminal(board):
        break

    print("\nAI thinking...")
    nodes = call_count = 0
    ai_move, val = minimax(board)

    board[ai_move] = X
    move_count += 1
    print(f"AI Move: {ai_move} (Value: {val})")
    print_game_stats()


print("\nGAME OVER")
print_board(board)

w = winner(board)
print(f"WINNER: {w}" if w else "It's a DRAW!")
print(f"Total moves: {move_count}")

print("\nSEARCH TREE")
print_tree_simple(create_board(), max_depth=2)