import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()

lower_case = s.str.lower()

string_length = s.str.len()

print("Original Series:")
print(s)
print("\nUppercase Conversion:")
print(upper_case)
print("\nLowercase Conversion:")
print(lower_case)
print("\nLength of Each String:")
print(string_length)
