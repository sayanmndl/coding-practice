import numpy as np


class TwoLayerMLP:

    def __init__(self, d_in, d_hidden, n_classes, lr=0.1):
        self.W1 = 0.01 * np.random.randn(d_in, d_hidden)
        self.b1 = np.zeros(d_hidden)

        self.W2 = 0.01 * np.random.randn(d_hidden, n_classes)
        self.b2 = np.zeros(n_classes)

        self.lr = lr

    def relu(self, Z):
        return np.maximum(0, Z)

    def softmax(self, logits):
        shifted = logits - np.max(
            logits, axis=1, keepdims=True
        )

        exp_logits = np.exp(shifted)

        return exp_logits / np.sum(
            exp_logits, axis=1, keepdims=True
        )

    def forward(self, X):
        """
        X: (n, d_in)
        """

        Z1 = X @ self.W1 + self.b1          # (n, h)
        A1 = self.relu(Z1)                  # (n, h)

        Z2 = A1 @ self.W2 + self.b2         # (n, C)
        probs = self.softmax(Z2)            # (n, C)

        return Z1, A1, Z2, probs

    def loss(self, X, y):
        _, _, _, probs = self.forward(X)

        n = X.shape[0]
        correct_probs = probs[np.arange(n), y]

        return -np.mean(
            np.log(np.clip(correct_probs, 1e-12, 1.0))
        )

    def fit(self, X, y, epochs=1000):
        n = X.shape[0]

        for _ in range(epochs):

            # ---------- Forward ----------
            Z1, A1, Z2, probs = self.forward(X)

            # ---------- Output layer ----------
            dZ2 = probs.copy()              # (n, C)
            dZ2[np.arange(n), y] -= 1
            dZ2 /= n

            dW2 = A1.T @ dZ2                # (h, C)
            db2 = np.sum(dZ2, axis=0)       # (C,)

            # ---------- Hidden layer ----------
            dA1 = dZ2 @ self.W2.T           # (n, h)

            dZ1 = dA1 * (Z1 > 0)            # (n, h)

            dW1 = X.T @ dZ1                 # (d, h)
            db1 = np.sum(dZ1, axis=0)       # (h,)

            # ---------- Update ----------
            self.W1 -= self.lr * dW1
            self.b1 -= self.lr * db1

            self.W2 -= self.lr * dW2
            self.b2 -= self.lr * db2

        return self

    def predict_proba(self, X):
        _, _, _, probs = self.forward(X)
        return probs

    def predict(self, X):
        _, _, Z2, _ = self.forward(X)

        # softmax not needed for argmax
        return np.argmax(Z2, axis=1)