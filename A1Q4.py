numbers = list(range(1, 10001))

equiv_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

for num in numbers:
    remainder = num % 5
    equiv_classes[remainder].append(num)


reconstructed_numbers = []
for key in equiv_classes:
    reconstructed_numbers.extend(equiv_classes[key])

reconstructed_numbers.sort()

is_valid = (reconstructed_numbers == numbers)

print("Equivalence Classes (mod 5):")
for key in equiv_classes:
    print(f"Class [{key}]: {equiv_classes[key][:10]} ...")

print("\nAre the equivalence classes valid?", is_valid)