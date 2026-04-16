import numpy as np

N = 20
cartesian_points = np.random.rand(N, 2) * 10  

x = cartesian_points[:, 0]
y = cartesian_points[:, 1]

r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)  

polar_coordinates = np.vstack((r, theta)).T

print("Cartesian Coordinates (x, y):")
print(cartesian_points)
print("\nPolar Coordinates (r, theta):")
print(polar_coordinates)
