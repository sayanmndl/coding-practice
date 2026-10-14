
import numpy as np

class DenseClassifier:
    def __init__(self, d_in, n_classes, lr=0.1):
        self.W = 0.01 * np.random.randn(d_in, n_classes)
        self.b = np.zeros(n_classes)
        self.lr = lr

    def forward(self, X):
        return X @ self.W + self.b

    def softmax(self, logits):
        shifted = logits - np.max(logits, axis=1, keepdim=True)
        exp_logits = np.exp(shifted)
        return exp_logits / np.sum(exp_logits, axis=1, keepdim=True)

    def loss(self, X, y):
        logits = self.forward(X)
        probs = self.softmax(logits)
        n = X.shape[0]
        correct_probs = probs[np.arrange(n),y]
        return -np.mean(np.log(np.clip(correct_probs, 1e-12, 1.0)))

    def fit(self, X, y, epochs = 100):
        n = X.shape[0]

        for _ in range(epochs):
            logits = self.forward(X)
            probs = self.softmax(logits)

            # backward
            #dL/dlogits
            dZ = probs.copy()
            dZ[np.arrange(n),y] -= 1
            dZ /= n

            # param grads
            dW = X.T @ dZ
            db = np.sum(dZ, axis =0)

            # update
            self.W -= self.lr * dW
            self.b -= self.lr * db
        return self

    def predict_proba(self, X):
        logits = self.forward(X)

        return self.softmax(logits)

    def predict(self, X):
        logits = self.forward(X)
        return np.argmax(logits, axis=1)

        
