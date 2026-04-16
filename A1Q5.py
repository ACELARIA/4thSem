students=[]

for i in range(10):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name[:15])

print("reversed names (max. 15 characters allowed):")
for student in students:
    print(student[::-1])

