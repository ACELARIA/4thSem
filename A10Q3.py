import numpy as np

def generate_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)

    if n % 2 == 1:
        row, col = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[row, col] = num
            new_row, new_col = (row - 1) % n, (col + 1) % n
            if magic_square[new_row, new_col]:
                row = (row + 1) % n
            else:
                row, col = new_row, new_col
    elif n % 4 == 0:
        for i in range(n):
            for j in range(n):
                magic_square[i, j] = (n * i + j + 1)
        for i in range(n):
            for j in range(n):
                if (i // (n // 4)) % 2 == (j // (n // 4)) % 2:
                    magic_square[i, j] = n * n + 1 - magic_square[i, j]
    else:
        
        half_n = n // 2
        sub_square = generate_magic_square(half_n)
        magic_square[:half_n, :half_n] = sub_square
        magic_square[half_n:, half_n:] = sub_square + half_n**2
        magic_square[:half_n, half_n:] = sub_square + 2 * half_n**2
        magic_square[half_n:, :half_n] = sub_square + 3 * half_n**2

    return magic_square

magic_squares = {n: generate_magic_square(n) for n in [4, 5, 6, 7, 8]}

for n, square in magic_squares.items():
    print(f"Magic Square for N = {n}:")
    print(square)
    print("\n")
