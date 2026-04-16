def find_min_max(my_set):
  if not my_set:
    return None, None  

  return min(my_set), max(my_set)


my_set = {1, 2,3, 4, 5}
min_value, max_value = find_min_max(my_set)

print("Minimum value:", min_value)
print("Maximum value:", max_value)






def is_value_in_set(my_set, value):
  
  return value in my_set

my_set = {1, 2, 3, 4, 5}
value_to_check = 3

if is_value_in_set(my_set, value_to_check):
  print(f"{value_to_check} is present in the set.")
else:
  print(f"{value_to_check} is not present in the set.")