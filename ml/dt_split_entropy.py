import numpy as np

def entropy(y):
    if len(y)==0.0:
        return 0.0
    
    _, counts = np.unique(y, return_counts = True)
    probs = counts / len(y)

    return - np.sum(probs * np.log2(probs))

def best_split_entropy(X,y):

    n, d = X.shape

    parent_entropy = entropy(y)

    best_feature = None
    best_threshold = None
    best_info_gain = -float('inf')

    for feature in range(d):
        values = X[:,feature]

        if len(values) <= 1:
            continue

        thresholds = (values[:-1]+values[1:])/ 2.0

        for threshold in thresholds:
            left_mask = X[:,feature] <= threshold
            right_mask = ~left_mask

            y_left = y[left_mask]
            y_right = y[right_mask]

            if len(y_left) == 0 or len(y_right) == 0:
                continue

            child_entropy = (
                len(y_left)/n * entropy(y_left)
                + len(y_right)/n * entropy(y_right)
            )

            gain = parent_entropy - child_entropy

            if gain > best_info_gain:
                best_info_gain= gain
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold, best_info_gain
