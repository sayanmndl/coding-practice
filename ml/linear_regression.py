import numpy as np

class LinearRegression:
    def __init__(
        self,
        lr = 0.01,
        n_iters=1000,
        reg_strength = 0.0
        ):
        self.lr = lr
        self.n_iters = n_iters
        self.reg_strength = reg_strength

        self.w = None
        self.b = None

    def fit(self, X,y):
        n,d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0

        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.w) + self.b

            error = y_pred - y

            dw = (2/n) * np.dot(X.T, error)
            # L2 reg
            dw += (2*self.reg_strength) * self.w

            db = (2/n) * np.sum(error)

            self.w -= self.lr * dw
            self.b -= self.lr * db

        return self

    def predict(self, X):
        return np.dt(X, self.w) + self.b


    def fit_closed_form(self, X, y):
        X_aug = np.columns_stack([np.ones(X.shape[0]), X])

        theta = np.linalg.lstsq(X_aug, y, rcond = None)[0]

        self.b = theta[0]
        self.w = theta[1:]
        return self