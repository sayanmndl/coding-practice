import numpy as np

def hmm_forward(obs, start_prob, trans_prob, emit_prob):
    T= len(obs)
    K=len(start_prob)

    alpha = np.zeros((T,K))
    alpha[0] = start_prob * emit_prob[:,obs[0]]

    for t in range (1, T):
        for j in range(K):
            alpha[t,j] = (
                np.sum(alpha[t-1] * trans_prob[:,j]) * emit_prob[j, obs[t]]
            )
    return np.sum(alpha[-1])


