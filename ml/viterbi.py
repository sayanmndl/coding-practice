import numpy as np

def viterbi(obs, start_prob, trans_prob, emit_prob):
    """
    obs:        (T,) integer observation IDs
    start_prob: (K,)
    trans_prob: (K, K)
                trans_prob[i, j] = P(state_j | state_i)
    emit_prob:  (K, V)
                emit_prob[j, o] = P(obs=o | state_j)
    """
    eps = 1e-12

    log_start = np.log(start_prob + eps) # (K,)
    log_trans = np.log(trans_prob + eps)
    log_emit = np.log(emit_prob + eps)

    T = len(obs)
    K = len(start_prob)

    dp = np.full((T,K), -np.inf)
    back = np.zeros((T,K), dtype=int)

    # t =0
    dp[0] = log_start + log_emit[:,obs[0]]

    for t in range(1,T):
        for j in range(K):
            scores = dp[t-1] + log_trans[:,j]  # (K,)
            best_prev = np.argmax(scores)

            dp[t,j] = (
                scores[best_prev]
                + log_emit[j, obs[t]]
            )
            back[t,j] = best_prev

    # best final state
    last_state = np.argmax(dp[-1])

    # backtrack
    path = [last_state]

    for t in range(T-1, 0, -1):
        last_state = back[t, last_state]
        path.append(last_state)
    
    path.reverse()
    return np.array(path)
    