import numpy as np

# -----------------------------
# Dataset
# -----------------------------
data = np.array([
    [0.046,4.006],[-0.454,-0.706],[0.181,5.769],[0.739,4.741],[-0.11,5.179],
    [-0.235,0.271],[-0.265,5.257],[0.148,5.131],[0.458,5.164],[5.104,4.02],
    [-0.117,-0.117],[0.034,-0.712],[-0.351,4.836],[5.515,5.466],[-0.301,0.926],
    [5.411,4.39],[-0.196,4.268],[5.166,5.488],[0.181,4.677],[4.58,4.845],
    [0.121,-0.957],[-0.272,0.055],[0.79,0.384],[-0.506,0.157],[0.049,5.484],
    [0.003,4.883],[-0.232,-0.233],[-0.3,-0.146],[-0.862,-0.281],[4.76,4.907],
    [5.406,5.678],[4.964,5.502],[5.172,4.118],[-0.018,5.782],[-1.31,5.411],
    [4.942,4.849],[-0.007,-0.529],[5.369,5.086],[4.261,4.64],[-0.404,4.749],
    [4.447,4.402],[0.733,-0.113],[4.336,5.098],[5.162,4.807],[4.662,5.306],
    [0.044,4.85],[4.77,5.529],[-0.575,0.188],[0.248,-0.069],[0.324,0.762]
])

k = 3

# -----------------------------
# Helper Functions
# -----------------------------
def assign_clusters(data, centroids):
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def cluster_wise_ssd(data, centroids, labels, k):
    ssd_list = []
    for i in range(k):
        points = data[labels == i]
        ssd = np.sum((points - centroids[i]) ** 2)
        ssd_list.append(ssd)
    return ssd_list

# -----------------------------
# Gradient Descent Method
# -----------------------------
def gradient_descent_kmeans(data, k, lr=0.1, max_iter=100):
    centroids = data[np.random.choice(len(data), k, replace=False)]

    for _ in range(max_iter):
        labels = assign_clusters(data, centroids)

        new_centroids = []
        for i in range(k):
            points = data[labels == i]

            if len(points) > 0:
                gradient = -2 * np.sum(points - centroids[i], axis=0)
                updated = centroids[i] - lr * gradient / len(points)
                new_centroids.append(updated)
            else:
                new_centroids.append(centroids[i])

        new_centroids = np.array(new_centroids)

        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    labels = assign_clusters(data, centroids)
    return centroids, labels

# -----------------------------
# Newton-Raphson Method
# -----------------------------
def newton_method_kmeans(data, k, max_iter=10):
    centroids = data[np.random.choice(len(data), k, replace=False)]

    for _ in range(max_iter):
        labels = assign_clusters(data, centroids)

        new_centroids = []
        for i in range(k):
            points = data[labels == i]

            if len(points) > 0:
                # Direct mean (Newton step)
                new_centroids.append(np.mean(points, axis=0))
            else:
                new_centroids.append(centroids[i])

        new_centroids = np.array(new_centroids)

        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    labels = assign_clusters(data, centroids)
    return centroids, labels

# -----------------------------
# Run Both Methods
# -----------------------------
gd_centroids, gd_labels = gradient_descent_kmeans(data, k)
nr_centroids, nr_labels = newton_method_kmeans(data, k)

# -----------------------------
# Compute SSD
# -----------------------------
gd_cluster_ssd = cluster_wise_ssd(data, gd_centroids, gd_labels, k)
nr_cluster_ssd = cluster_wise_ssd(data, nr_centroids, nr_labels, k)

# -----------------------------
# Output
# -----------------------------
print("===== Gradient Descent Method =====")
print("Centroids:\n", gd_centroids)
print("Cluster-wise SSD:", [float(x) for x in gd_cluster_ssd])
print("Total SSD:", sum(gd_cluster_ssd))

print("\n===== Newton-Raphson Method =====")
print("Centroids:\n", nr_centroids)
print("Cluster-wise SSD:", [float(x) for x in nr_cluster_ssd])
print("Total SSD:", sum(nr_cluster_ssd))