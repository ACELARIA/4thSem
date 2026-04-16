def sum_of_list(lst):
 
  total = 0
  for num in lst:
    total += num
  return total

my_list = [1,1,1,1,1]
result = sum_of_list(my_list)
print("Sum of all items in the list:", result) 





def multiply_list_items(lst):
 
  product = 1
  for num in lst:
    product *= num
  return product

my_list = [1,1,1,1,1]
result = multiply_list_items(my_list)
print("Product of all items in the list:", result) 






def find_largest(numbers):
 
  if not numbers:
    return None  

  largest = numbers[0] 

  for num in numbers:
    if num > largest:
      largest = num

  return largest

my_list = [1,2,3,4,5]
largest_number = find_largest(my_list)

if largest_number is not None:
  print("The largest number in the list is:", largest_number)
else:
  print("The list is empty.")





  

def find_smallest(numbers):
 
  if not numbers:
    return None  

  smallest = numbers[0]  

  for num in numbers:
    if num < smallest:
      smallest = num

  return smallest

my_list = [1,2,3,4,5]
smallest_number = find_smallest(my_list)

if smallest_number is not None:
  print("The smallest number in the list is:", smallest_number)
else:
  print("The list is empty.")


