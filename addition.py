def perform_arithmetic_operations(num1, num2):
   
    addition = num1 + num2
    print("Addition:", addition)

    subtraction = num1 - num2
    print("Subtraction:", subtraction)

    multiplication = num1 * num2
    print("Multiplication:", multiplication)

    if num2 != 0:
        division = num1 / num2
        print("Division:", division)
    else:
        print("Error: Division by zero")

   
    exponentiation = num1**num2
    print("Exponentiation:", exponentiation)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

perform_arithmetic_operations(num1, num2)