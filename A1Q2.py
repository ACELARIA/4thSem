import random

random_sequence = [random.randint(0, 1) for _ in range(100)]

max_count = 0  
current_count = 0 

for num in random_sequence:
    if num == 0:
        current_count += 1
        if current_count > max_count:
            max_count = current_count  
    else:
        current_count = 0  

print("Random Sequence:")
print(random_sequence)

print("\nLongest run of zeros:", max_count)