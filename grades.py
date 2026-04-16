def calculate_grade(marks):
  if marks >= 90:
    return 'A'
  elif marks >= 80:
    return 'B'
  elif marks >= 70:
    return 'C'
  elif marks >= 60:
    return 'D'
  else:
    return 'F'

sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

grade = calculate_grade(percentage)

print("Total marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)