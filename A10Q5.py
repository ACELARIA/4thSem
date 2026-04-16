import numpy as np

arr = np.array(['arushi', 'atish', 'raj', 'aparna'])

length = 15

centered = np.char.center(arr, length, fillchar='_')

left_justified = np.char.ljust(arr, length, fillchar='_')

right_justified = np.char.rjust(arr, length, fillchar='_')

print("Original Array:")
print(arr)

print("\nCentered (padded with _):")
print(centered)

print("\nLeft-Justified (padded with _):")
print(left_justified)

print("\nRight-Justified (padded with _):")
print(right_justified)
