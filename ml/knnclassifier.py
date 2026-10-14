from collections import Counter
import numpy as np

class KNNClassifier:
    def __init__(self, k=3):
        if k<=0:
            raise ValueError
        
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y)

        if len(X) != len(y):
            raise

        if self.k > len(X):
            raise

        self.X_train = X
        self.y_train = y
        return self

    
    def _euclidean_dist(self, x1, x2):
        return np.sqrt(np.sum(x1-x2)**2)

    def _predict_single(self, x):

        # compute distance
        dist = np.array([
            self._euclidean_dist(x,x_train) for x_train in self.X_train
        ])

        k_indices = np.argsort(dist)[:self.k]
        k_labels = self.y_train[k_indices]

        most_common = Counter(k_labels).most_common(1)
        return most_common[0][0]

    def predict(self, X):
        X = np.asarray(X, dtype=float)

        return np.asarray([
            self._predict_single(x) for x in X
        ])


if __name__ == "__main__":
    X_train = [
        [1, 2],
        [1, 3],
        [2, 2],
        [6, 7],
        [7, 8],
        [6, 8],
    ]

    y_train = [0, 0, 0, 1, 1, 1]

    knn = KNNClassifier(k=3)
    knn.fit(X_train, y_train)

    X_test = [
        [1.5, 2.5],
        [6.5, 7.5],
    ]

    predictions = knn.predict(X_test)

    print(predictions)