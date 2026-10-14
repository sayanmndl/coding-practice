
from typing import Concatenate
import numpy as np

def softmax(x, axis = -1):
    #stable softmax
    x = x - np.max(x, axis=axis, keepdim=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=axis, keepdim=True)

def dot_product_attention(Q,K,V):
    scores = Q @ K.T / np.sqrt(K.shape[-1]) # scaled dot product

    weights = softmax(scores, axis=1)

    output = weights @ V
    return output, weights


def causal_attention(Q,K,V):
    n,d_k = K.shape

    scores = Q @ K.T / np.sqrt(d_k)

    # true above diagonal
    mask = np.triu(
        np.ones((n,n), dtype=bool),k=1
    )
    
    scores[mask] = -np.inf

    weights = softmax(scores, axis=-1)
    output = weights @ V
    return output, weights
    

def multi_head_attention(Q,K,V, num_heads):
    B,T,D = Q.shape
    d_head = B // num_heads

    Q = Q.reshape(B,T,num_heads, d_head).transpose(0, 2, 1, 3)
    K = K.reshape(B,T,num_heads, d_head).transpose(0, 2, 1, 3)
    V = V.reshape(B,T,num_heads, d_head).transpose(0, 2, 1, 3)

    # [B, H, T, d] @ [B, H, d, T] -> [B, H, T, T]
    scores = Q @ K.transpose(0,1,3,2)
    scores /= np.sqrt(d_head)

    scores -= np.max(scores, axis=-1, keepdims=True)
    weights = np.exp(scores)
    weights /= np.sum(weights, axis=-1, keepdims=True)

    # [B, H, T,T] @ [B,H,T,d] -> [B,H,T,d]
    out = weights @ V

    # [BHTd] -> [BTHd]
    out = out.transpose(0,2,1,3)

    # Concatenate
    out = out.reshape(B,T,D)
    return out


    