import random
import itertools

# Cost Matrix for cities A-H (0-7)
COST_MATRIX = [
    [0, 10, 15, 20, 25, 30, 35, 40],
    [12, 0, 35, 15, 20, 25, 30, 45],
    [25, 30, 0, 10, 40, 20, 15, 35],
    [18, 25, 12, 0, 15, 30, 20, 10],
    [22, 18, 28, 20, 0, 15, 25, 30],
    [35, 22, 18, 28, 12, 0, 40, 20],
    [30, 35, 22, 18, 28, 32, 0, 15],
    [40, 28, 35, 22, 18, 25, 12, 0 ]
]

def calculate_total_cost(path):
    #Calculates the total distance of a TSP tour including return to start.
    cost = 0
    for i in range(len(path) - 1):
        cost += COST_MATRIX[path[i]][path[i+1]]
    cost += COST_MATRIX[path[-1]][path[0]] # Return to the first city
    return cost

def get_neighbors(path):
    # Generates all neighbors by swapping two cities in the path.
    neighbors = []
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            neighbor = list(path)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(tuple(neighbor))
    return neighbors

def local_beam_search(k, max_iterations=100):
    num_cities = len(COST_MATRIX)
    
    # 1. Initialize k random states
    current_states = []
    for _ in range(k):
        path = list(range(num_cities))
        random.shuffle(path)
        current_states.append(tuple(path))
    
    for iteration in range(max_iterations):
        all_neighbors = []
        
        # 2. Generate all neighbors for all current states
        for state in current_states:
            all_neighbors.extend(get_neighbors(state))
        
        # Remove duplicates to maintain diversity
        all_neighbors = list(set(all_neighbors))
        
        # 3. Score all neighbors and sort by cost (ascending)
        scored_neighbors = [(n, calculate_total_cost(n)) for n in all_neighbors]
        scored_neighbors.sort(key=lambda x: x[1])
        
        # 4. Select the best k neighbors
        next_states = [s for s, cost in scored_neighbors[:k]]
        best_cost = scored_neighbors[0][1]
        
        # Check for convergence: if the best k don't change, we stop
        if set(next_states) == set(current_states):
            break
            
        current_states = next_states
        
    return current_states[0], best_cost

# Comparative Analysis
beam_widths = [3, 5, 10]
print(f"{'Beam Width (k)':<15} | {'Best Cost Found':<15} | {'Path Sample'}")
print("-" * 60)

for k in beam_widths:
    best_path, cost = local_beam_search(k)
    # Mapping indices back to letters for readability
    city_names = "ABCDEFGH"
    readable_path = " -> ".join([city_names[i] for i in best_path]) + f" -> {city_names[best_path[0]]}"
    print(f"{k:<15} | {cost:<15} | {readable_path}")