import numpy as np

def gini(y):
    # for singl node
    # gini = 1 - sum(p_i^2)
    # = sum(p_i * (1 - p_i))

    # for a split
    # gini_split = sum(p_i * (1 - p_i)) for each child node

    _, counts = np.unique(y, return_counts = True)
    p = counts / len(y)
    return 1 - sum(p**2)

def entropy(y):
    labels, counts = np.unique(y, return_counts = True)
    p = counts / len(y)
    return - np.sum(p * np.log2(p))

def information_gain(parent, left, right):
    n = len(parent)
    
    return entropy(parent) \
    - (len(left) / n * entropy(left)) \
        - (len(right) / n * entropy(right))

