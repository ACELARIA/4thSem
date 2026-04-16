#Find factorial of a number
def factorial(n):
  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

num = int(input("Enter an integer: "))

result = factorial(num)
print("The factorial of", num, "is", result)