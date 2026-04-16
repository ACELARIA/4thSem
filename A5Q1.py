def maxXor(L,R):
    max_xor = 0
    for a in range(L, R + 1):
        for b in range(a, R + 1):
            max_xor = max(max_xor,a^b)
    return max_xor

L = int(input("Enter 1st integer: "))
R = int(input("Enter 2nd integer: "))

print(maxXor(L,R))
