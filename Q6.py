def reverse_number(n):
  reversed = 0
  while n > 0:
    remainder = n % 10
    reversed= (reversed * 10) + remainder
    n//= 10

  return reversed

n = int(input("Enter an integer: "))
reversed_number = reverse_number(n)
print("The reversed number is:", reversed_number)