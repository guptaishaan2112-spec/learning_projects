import numpy as np
#kmeans clustering algorithm
class KMeans:
    def __init__(self, k=3, max_iter=100):
        self.k = k
        self.max_iter = max_iter
    def fit(self, x):
        self.x = x
        m = x.shape[0]
        all_j = []
        centroids = np.zeros((10, self.k,x.shape[1]))
        for run in range(10):
            u_random = x[np.random.choice(x.shape[0], size = self.k, replace = False)]
            for p in range(self.max_iter):
                c_assigned = np.zeros(m, dtype=int)
                for i in range(m):
                    xi = x[i]
                    dist = []
                    for u in u_random:
                        sq_dist = np.sum((xi - u)**2)
                        dist.append(sq_dist)
                    c = dist.index(min(dist))
                    c_assigned[i] = c
                new_u = np.zeros((self.k, x.shape[1]))
                for j in range(self.k):
                    x_target_indexes = np.where(np.array(c_assigned) == j)[0]
                    x_target = x[x_target_indexes]
                    new_u[j] = np.mean(x_target, axis=0)
                u_random = new_u
            sq_dist = np.sum((x - new_u[c_assigned])**2)
            all_j.append(sq_dist)
            centroids[run] = new_u
        best_j = min(all_j)
        best_centroids = centroids[all_j.index(best_j),:]
        return best_centroids, best_j    
                
    