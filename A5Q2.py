def max_pieces(K):
 a=K//2
 b = K-a
 return a*b
T = int(input("Input number: "))

for _ in range(T):
    K = int(input("Input number of cuts: "))
    print(max_pieces(K))
