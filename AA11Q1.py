    # Map Coloring using Backtracking (CSP)

# Districts (as per image)
districts = [
    "Kucchh", "Banaskantha", "Patan", "Mehsana", "Sabarkantha",
    "Gandhi Nagar", "Ahmedabad", "Surendranagar", "Rajkot",
    "Jamnagar", "Porbandar", "Junagadh", "Amreli", "Bhavnagar",
    "Anand", "Kheda", "Panchmahal", "Dahod", "Vadodara",
    "Bharuch", "Narmada", "Surat"
]

# Adjacency list (based on map)
neighbors = {
    "Kucchh": ["Banaskantha", "Surendranagar", "Jamnagar"],
    "Banaskantha": ["Kucchh", "Patan", "Sabarkantha"],
    "Patan": ["Banaskantha", "Mehsana", "Surendranagar"],
    "Mehsana": ["Patan", "Sabarkantha", "Gandhi Nagar"],
    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhi Nagar"],
    "Gandhi Nagar": ["Mehsana", "Sabarkantha", "Ahmedabad", "Kheda"],
    "Ahmedabad": ["Gandhi Nagar", "Kheda", "Anand", "Surendranagar"],
    "Surendranagar": ["Kucchh", "Patan", "Ahmedabad", "Rajkot", "Bhavnagar"],
    "Rajkot": ["Surendranagar", "Jamnagar", "Junagadh", "Amreli"],
    "Jamnagar": ["Kucchh", "Rajkot", "Porbandar"],
    "Porbandar": ["Jamnagar", "Junagadh"],
    "Junagadh": ["Porbandar", "Rajkot", "Amreli"],
    "Amreli": ["Rajkot", "Junagadh", "Bhavnagar"],
    "Bhavnagar": ["Surendranagar", "Amreli", "Anand"],
    "Anand": ["Ahmedabad", "Bhavnagar", "Kheda", "Vadodara"],
    "Kheda": ["Gandhi Nagar", "Ahmedabad", "Anand", "Panchmahal"],
    "Panchmahal": ["Kheda", "Dahod", "Vadodara"],
    "Dahod": ["Panchmahal"],
    "Vadodara": ["Anand", "Panchmahal", "Bharuch"],
    "Bharuch": ["Vadodara", "Narmada", "Surat"],
    "Narmada": ["Bharuch", "Surat"],
    "Surat": ["Bharuch", "Narmada"]
}

# Colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Check if safe
def is_safe(district, color, assignment):
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking
def solve(assignment):
    if len(assignment) == len(districts):
        return True

    for district in districts:
        if district not in assignment:
            break

    for color in colors:
        if is_safe(district, color, assignment):
            assignment[district] = color

            if solve(assignment):
                return True

            del assignment[district]

    return False

# Run
assignment = {}
if solve(assignment):
    print("Solution:")
    for d in assignment:
        print(d, "->", assignment[d])
else:
    print("No solution found")