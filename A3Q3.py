def utopian_tree_growth(T, cycles):
    for N in cycles:
        height = 1  
        for cycle in range(1, N + 1):  
            if cycle % 2 == 1:  
                height *= 2
            else:  
                height += 1
        print(height)

T = int(input("Input:"))  
cycles = [int(input()) for _ in range(T)]  

utopian_tree_growth(T, cycles)
