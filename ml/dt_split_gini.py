
import numpy as np

def gini(y):
    if len(y) == 0:
        return 0.0
    
    classes, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)

    return 1.0 - np.sum(probs ** 2)

def best_split_gini(X,y):
    n,d = X.shape

    best_feature = None
    best_threshold = None
    best_impurity = float('inf')

    for feature in range(d):
        values = np.unique(X[:, feature])

        if len(values) <= 1:
            continue

        thresholds = (values[:-1] + values[1:]) / 2.0

        for threshold in thresholds:
            left_mask = X[:, feature] <=threshold
            right_mask = ~left_mask

            y_left = y[left_mask]
            y_right = y[right_mask]

            if len(y_left) == 0 or len(y_right) == 0:
                continue

            left_weight = len(y_left)/n
            right_weight = len(y_right)/n

            impurity = (left_weight * gini(y_left) + right_weight * gini(y_right))

            if impurity < best_impurity:
                best_impurity = impurity
                best_feature = feature
                best_threshold = threshold

        return best_feature, best_threshold, best_impurity 
