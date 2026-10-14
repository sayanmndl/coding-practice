import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.1, n_iters=1000, reg_strength=0.0):
        self.lr = lr
        self.n_iters = n_iters
        self.reg_strength= reg_strength

        self.w = None
        self.b = None


    def _sigmoid(self, z):
        z = np.clip(z, -500, 500)
        return 1.0 / (1.0 + np.exp(-z))

    def fit(self, X, y):
        n,d = X.shape

        self.w = np.zeros(d)
        self.b = 0.0

        for _ in range(self.n_iters):

            z = np.dot(X, self.w) + self.b # X @ self.w + self.b

            p = self._sigmoid(z) # (n,)

            error = p - y  # dL/dz

            dw = np.dot(X.T, error) / n # X.T @ dL/dz / n
            # L2 reg
            dw += (self.reg_strength / n) * self.w

            db = np.mean(error) # dL/dz

            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict_proba(self, X):
        z = X @ self.w + self.b
        return self._sigmoid(z)

    def predict(self,X,thresh=0.5):
        proba = self.predict_proba(X)
        return (proba >= thresh).astype(int)