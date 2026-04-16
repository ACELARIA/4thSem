def solve_send_more_money():
    solutions = []

    # Since MONEY is 5-digit → M must be 1
    M = 1

    # Try possible values
    for S in range(1, 10):
        if S == M:
            continue

        for E in range(10):
            if E in (S, M):
                continue

            for N in range(10):
                if N in (S, M, E):
                    continue

                for D in range(10):
                    if D in (S, M, E, N):
                        continue

                    # ---- Column 1: D + E = Y + 10*c1 ----
                    for Y in range(10):
                        if Y in (S, M, E, N, D):
                            continue

                        c1 = (D + E) // 10
                        if (D + E) % 10 != Y:
                            continue

                        for R in range(10):
                            if R in (S, M, E, N, D, Y):
                                continue

                            # ---- Column 2: N + R + c1 = E + 10*c2 ----
                            c2 = (N + R + c1) // 10
                            if (N + R + c1) % 10 != E:
                                continue

                            for O in range(10):
                                if O in (S, M, E, N, D, Y, R):
                                    continue

                                # ---- Column 3: E + O + c2 = N + 10*c3 ----
                                c3 = (E + O + c2) // 10
                                if (E + O + c2) % 10 != N:
                                    continue

                                # ---- Column 4: S + M + c3 = O + 10*c4 ----
                                c4 = (S + M + c3) // 10
                                if (S + M + c3) % 10 != O:
                                    continue

                                # Final constraint: c4 must equal M (which is 1)
                                if c4 != M:
                                    continue

                                # Valid solution
                                solutions.append((S, E, N, D, M, O, R, Y))

    # Print results
    for S, E, N, D, M, O, R, Y in solutions:
        SEND  = 1000*S + 100*E + 10*N + D
        MORE  = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        print(f"S={S} E={E} N={N} D={D} M={M} O={O} R={R} Y={Y}")
        print(f"  {SEND}")
        print(f"+ {MORE}")
        print("------")
        print(f"  {MONEY}")


# Run
solve_send_more_money()