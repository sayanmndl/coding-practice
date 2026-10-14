import numpy as np

class MultinomialNaiveBayes:
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
        self.classes = np.unique(y)
        n,d = X.shape

        self.log_priors = np.zeros(len(self.classes))
        self.log_likelihoods = np.zeros((len(self.classes), d))

        for i, c in enumerate(self.classes):
            X_c = X[y==c] # (n_c, d)

            self.log_priors[i] = np.log(len(X_c) /n)
            
            feature_counts = np.sum(X_c, axis = 0) # (d, 
            smoothed = feature_counts + self.alpha

            probs = smoothed / (np.sum(feature_counts) + self.alpha*d)

            self.log_likelihoods[i] = np.log(probs)

        return self

    def predict(self, X):
        scores = (np.dot(X, self.log_likelihoods.T) + self.log_priors)
        best = np.argmax(scores, axis=1)
        return self.classes(best)