import numpy as np

def softmax(logits):
    # logits: (n,C)
    shifted = logits - np.max(logits, axis=1, keepdims=True)

    exp_logits = np.exp(shifted)

    probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

    return probs


def cross_entropy_loss(logits, y):

    n, C = logits.shape
    probs = softmax(logits)

    # probability of correct class
    correct_probs = probs[np.arrange(n), y]

    loss = -np.mean(np.log(np.clip(correct_probs, 1e-12, 1.0)))

    grad = probs.copy()
    grad[np.arrange(n),y] -=1
    grad /= n

    return loss, grad