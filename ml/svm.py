import numpy as np


class LinearSVMClassifier:

    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        """
        Initialize hyper-parameters.
        lambda_param: Regularization parameter balancing margin size vs error.
        """
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None  # Weights vector
        self.b = None  # Bias scalar

    def fit(self, X, y):
        """
        Train the linear SVM using Stochastic Gradient Descent.
        """
        X = np.array(X)
        y = np.array(y)
        # Convert labels from {0, 1} to {-1, 1} for SVM hinge loss math
        y_transformed = np.where(y <= 0, -1, 1)

        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0.0

        # Optimization loop
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                # Check the margin condition: y * (w · x + b) >= 1
                condition = y_transformed[idx] * (np.dot(x_i, self.w) + self.b) >= 1

                if condition:
                    # Point is correctly classified outside the margin.
                    # Update weights only with regularization gradient.
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    # Point is a support vector misclassified or inside the margin.
                    # Update weights and bias with regularizer + hinge loss gradients.
                    self.w -= self.lr * (
                        2 * self.lambda_param * self.w
                        - np.dot(x_i, y_transformed[idx])
                    )
                    self.b -= self.lr * (-y_transformed[idx])

    def predict(self, X):
        """
        Predict binary labels for a dataset.
        """
        X = np.array(X)
        # Compute the raw hyperplane projection
        linear_output = np.dot(X, self.w) + self.b
        # Map back from {-1, 1} signum space to standard binary {0, 1} labels
        return np.where(linear_output >= 0, 1, 0)


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    # Linearly separable mock dataset (2 features)
    X_train = [[1, 2], [2, 3], [5, 6], [6, 7]]
    y_train = [0, 0, 1, 1]

    # Initialize and fit the Linear SVM
    svm = LinearSVMClassifier(learning_rate=0.001, lambda_param=0.01, n_iters=1000)
    svm.fit(X_train, y_train)

    # Out-of-sample data points to test
    X_test = [[1.5, 2.5], [6.5, 7.5]]

    # Generate predictions
    predictions = svm.predict(X_test)

    print(f"Weights (w): {svm.w}")
    print(f"Bias (b): {svm.b}")
    print(f"Predicted Classes: {predictions}")
    # Expected output: Predicted Classes: [0 1]
