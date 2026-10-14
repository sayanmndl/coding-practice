
import numpy as np

class KMeans:
    def __init__(self, k =3, max_iters = 100, tol=1e-4, random_state=None):
        self.k = k
        self.max_iters=max_iters
        self.tol=tol
        self.random_state=random_state

        self.centrods = None
        self.labels_ = None

    def fit(self, X):
        X=np.asarray(X,dtype=float)

        n_samples = X.shape[0]

        if self.k <= 0 or self.k > n_samples:
            raise ValueError

        rng = np.random.default_rng(self.random_state)

        #randomly choose k initially
        indices = rng.choice(n_samples, size=self.k, replace=False)
        self.centroids = X[indices].copy()

        for _ in range(self.max_iters):

            # label assignment
            dist = self._compute_dist(X)
            labels = np.argmin(dist, axis=1)

            new_centroids = np.empty_like(self.centroids)

            for cluster_id in range(self.k):
                cluster_points = X[labels == cluster_id]

                if len(cluster_points) > 0:
                    new_centroids[cluster_id] = cluster_points.mean(axis=0)
                else:
                    # empty cluster -> reinitialize to a random data point
                    new_centroids[cluster_id] = X[rng.intergers(0,n_samples)]

                # check convergence
                shift = np.linalg.norm(new_centroids - self.centroids)
                self.centroids = new_centroids

                if shift < self.tol:
                    break
        
        # recompute final labels
        self.labels_ = np.argmin(self._compute_dist(X), axis=1)

        return self

    def _compute_dist(self, X):
        # returns dist shape: (n_samples, k)
        diff = X[:, None, :] - self.centroids[None,:,:]
        return np.sum(diff**2, axis=2)

    def predict(self, X):
        if self.centroids==None:
            raise ValueError

        X = np.asarray(X,dtype=float)

        dist = self._compute_dist(X)
        return np.argmin(dist, axis=1)

if __name__ == "__main__":

    X = np.array([
        [1.0, 1.0],
        [1.5, 2.0],
        [3.0, 4.0],
        [5.0, 7.0],
        [3.5, 5.0],
        [4.5, 5.0],
        [3.5, 4.5]
    ])

    model = KMeans(
        k=2,
        random_state=42
    )

    model.fit(X)

    print("Centroids:")
    print(model.centroids)

    print("Labels:")
    print(model.labels_)