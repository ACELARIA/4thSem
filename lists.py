my_list = [1,2,3,1,2,3]

print("My sorted list:",sorted(my_list))
print("My original list:",my_list)


my_list.insert(1,0)
print("After inserting:", my_list)

my_list.remove(3)
print("After removing 3:", my_list)

my_list.append(6)
print("After appending 6:", my_list)

length = len(my_list)
print("Length of the list:", length)

last_element = my_list.pop()
print("Popped element:", last_element)
print("List after popping:", my_list)

my_list.sort()
print("After sorting the list:", my_list)

my_list.sort(reverse=True)
print("After sorting the list:", my_list)

my_list.clear()
print("After clearing the list:", my_list)
