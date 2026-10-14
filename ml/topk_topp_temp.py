
import numpy as np


def softmax(x):
    x = x - np.max(x)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)


def top_k_sample(logits, k):
    V = logits.shape[0] # (V,)
    if k < 1 or k > V:
        raise ValueError
    
    top_idx = np.argpartition(logits, -k)[-k:]
    filtered = np.full_like(logits, -np.inf, dtype=float)
    filtered[top_idx] = logits[top_idx]

    probs = softmax(filtered)
    token = np.random.choice(V, p=probs)
    return token

def top_p_sample(logits, p):

    if not (0 < p <= 1):
        raise ValueError
    
    probs = softmax(logits)

    sorted_idx = np.argsort(probs)[::-1]
    sorted_probs = probs[sorted_idx]

    cumulative = np.cumsum(sorted_probs)
    cutoff = np.searchsorted(cumulative,p)

    keep_idx = sorted_idx[:cutoff+1]
    keep_probs = probs[keep_idx]

    keep_probs = keep_probs / keep_probs.sum()
    token = np.random.choice(keep_idx, p = keep_probs)
    return token


def temperature_sample(logits, temperature=1.0):
    """
    logits: (V,)
    temperature: > 0
    """

    if temperature <= 0:
        raise ValueError("temperature must be > 0")

    scaled_logits = logits / temperature

    probs = softmax(scaled_logits)

    token = np.random.choice(
        len(logits),
        p=probs
    )

    return token