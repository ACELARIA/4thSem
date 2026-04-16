def convert_length(feet, choice):
  conversion_factors = {
      1: 12,        
      2: 0.333333,  
      3: 0.000189394,  
      4: 304.8,     
      5: 30.48,     
      6: 0.3048,     
      7: 0.0003048
  }

  if choice in conversion_factors:
    converted_value = feet * conversion_factors[choice]
    unit_names = ["Inches", "Yards", "Miles", "Millimeters", "Centimeters", "Meters", "Kilometers"]
    units = unit_names[choice - 1]
    return converted_value, units
  else:
    return None, "Invalid choice"

feet = float(input("Enter length in feet: "))
choice = int(input("Select conversion:\n"
                   "1. Inches\n"
                   "2. Yards\n"
                   "3. Miles\n"
                   "4. Millimeters\n"
                   "5. Centimeters\n"
                   "6. Meters\n"
                   "7. Kilometers\n"
                   "Enter your choice: "
                  ))

result, unit = convert_length(feet, choice)

if result is not None:
  print(f"{feet} feet is equal to {result} {unit}")
else:
  print(unit)