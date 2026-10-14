import numpy as np


class DecisionTree:
    class Node:
        def __init__(
            self,
            feature=None,
            threshold=None,
            left=None,
            right=None,
            value=None
        ):
            self.feature = feature
            self.threshold = threshold
            self.left = left
            self.right = right
            self.value = value

        def is_leaf(self):
            return self.value is not None

    def __init__(
        self,
        max_depth=5,
        min_samples_split=2,
        criterion="gini"
    ):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.criterion = criterion
        self.root = None

    def fit(self, X, y):
        self.root = self._build_tree(X, y, depth=0)

    def predict(self, X):
        return np.array([
            self._traverse_tree(x, self.root)
            for x in X
        ])

    # --------------------------------------------------
    # Tree construction
    # --------------------------------------------------

    def _build_tree(self, X, y, depth):
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))

        # stopping conditions
        if (
            depth >= self.max_depth
            or n_samples < self.min_samples_split
            or n_classes == 1
        ):
            return self.Node(value=self._majority_class(y))

        best_feature, best_threshold = self._best_split(X, y)

        # no useful split found
        if best_feature is None:
            return self.Node(value=self._majority_class(y))

        left_mask = X[:, best_feature] <= best_threshold
        right_mask = ~left_mask

        left = self._build_tree(
            X[left_mask],
            y[left_mask],
            depth + 1
        )

        right = self._build_tree(
            X[right_mask],
            y[right_mask],
            depth + 1
        )

        return self.Node(
            feature=best_feature,
            threshold=best_threshold,
            left=left,
            right=right
        )

    # --------------------------------------------------
    # Find best split
    # --------------------------------------------------

    def _best_split(self, X, y):
        n_samples, n_features = X.shape

        best_score = -np.inf
        best_feature = None
        best_threshold = None

        for feature in range(n_features):

            values = np.unique(X[:, feature])

            # candidate split points between adjacent values
            thresholds = (
                values[:-1] + values[1:]
            ) / 2

            for threshold in thresholds:

                left_mask = X[:, feature] <= threshold
                right_mask = ~left_mask

                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue

                score = self._split_score(
                    y,
                    y[left_mask],
                    y[right_mask]
                )

                if score > best_score:
                    best_score = score
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    # --------------------------------------------------
    # Split scoring
    # --------------------------------------------------

    def _split_score(self, parent, left, right):

        if self.criterion == "gini":
            return self._gini_gain(parent, left, right)

        elif self.criterion == "information_gain":
            return self._information_gain(parent, left, right)

        else:
            raise ValueError(
                "criterion must be 'gini' or 'information_gain'"
            )

    # --------------------------------------------------
    # Gini
    # --------------------------------------------------

    def _gini(self, y):
        if len(y) == 0:
            return 0

        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)

        return 1 - np.sum(probabilities ** 2)

    def _gini_gain(self, parent, left, right):
        n = len(parent)

        weighted_child_impurity = (
            len(left) / n * self._gini(left)
            +
            len(right) / n * self._gini(right)
        )

        return (
            self._gini(parent)
            - weighted_child_impurity
        )

    # --------------------------------------------------
    # Entropy / Mutual Information
    # --------------------------------------------------

    def _entropy(self, y):
        if len(y) == 0:
            return 0

        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)

        return -np.sum(
            probabilities
            * np.log2(probabilities)
        )

    def _information_gain(self, parent, left, right):
        n = len(parent)

        child_entropy = (
            len(left) / n * self._entropy(left)
            +
            len(right) / n * self._entropy(right)
        )

        return (
            self._entropy(parent)
            - child_entropy
        )

    # --------------------------------------------------
    # Prediction helpers
    # --------------------------------------------------

    def _majority_class(self, y):
        values, counts = np.unique(y, return_counts=True)
        return values[np.argmax(counts)]

    def _traverse_tree(self, x, node):

        if node.is_leaf():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)

        return self._traverse_tree(x, node.right)