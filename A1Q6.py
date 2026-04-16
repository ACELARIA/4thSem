import math

points = []
for i in range(10):
    x, y, z = map(float, input(f"Enter coordinates for point {i+1} (x y z): ").split())
    points.append((x, y, z))

nearest_neighbors = []

for i in range(10):
    min_dist = float('inf')
    nearest = None
    for j in range(10):
        if i == j:
            continue  

        dist = math.dist(points[i], points[j])

        if dist < min_dist:
            min_dist = dist
            nearest = points[j]
    nearest_neighbors.append((points[i], nearest))

for point, neighbor in nearest_neighbors:
    print(f"Point: {point}, Nearest Neighbour: {neighbor}")