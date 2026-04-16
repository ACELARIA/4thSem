N = int(input("Enter a number: "))
count = 0
for i, digit in enumerate(str(N)):
    if digit != '0' and N % int(digit) == 0:
        count += 1
print("Number of positions where digits exactly divides N:", count)