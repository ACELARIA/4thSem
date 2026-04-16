my_tuple = (10, "hello", 3.99, True, 50)

print("Second item in the tuple:", my_tuple[1])

def add_to_tuple(original_tuple, new_item):
 return original_tuple + (new_item,)

my_tuple = (1,1,1)
new_item = 2
updated_tuple = add_to_tuple(my_tuple, new_item)

print("Original tuple:", my_tuple)
print("Updated tuple:", updated_tuple)


def replace_last_value(tuple_list, new_value):
  return [tuple(t[:-1]) + (new_value,) for t in tuple_list]

my_list = [(10,20,40),(40,50,60),(70,80,90)]
new_value = 100
result = replace_last_value(my_list, new_value)
print("Original list:", my_list)
print("Updated list:", result)


def remove_empty_tuples(tuple_list):
 return [t for t in tuple_list if t]

my_list = [(),(),('a','b'), ('a','b','c'),('d')]
result = remove_empty_tuples(my_list)
print("Original list:", my_list)
print("List without empty tuples:", result)


