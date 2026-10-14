class PCA:
    def __init__(self, n_components):
        self.n_components = n_components

    def fit(self,X):
        n, d = X.shape
        self.mean = np.mean(X, axis = 0)
        Xc = X - self.mean
        cov = (Xc.T @ Xc) / (n-1)
        eigvals, eigvecs = np.linalg.eigh(cov)
        idx = np.argsort(eigvals)[::-1]
        self.components = eigvecs[:, idx[:self.n_components]]
        self.explained_variance = eigvals[idx[:self.n_components]]

        return self

    def trasnform(self, X):
        return (X - self.mean) @ self.components