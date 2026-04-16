def next_permutation(w):
    w = list(w)
    n = len(w)
    
    k = n - 2
    while k >= 0 and w[k] >= w[k + 1]:
        k -= 1
    
    if k == -1:
        return "no answer"
    
    l = n - 1
    while w[l] <= w[k]:
        l -= 1
    
    w[k], w[l] = w[l], w[k]
    w = w[:k + 1] + w[k + 1:][::-1]
    
    return ''.join(w)

t = int(input("Enter number of letters : "))
for _ in range(t):
    w = input("Enter letters: ").strip()
    print(next_permutation(w))
