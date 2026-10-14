import numpy as np

def greedy_decode(model, start_token, eos_token, max_len):
    tokens = [start_token]

    for _ in range(max_len):
        logits = model(tokens)
        next_token = int(np.argmax(logits))
        tokens.append(next_token)

        if next_token == eos_token:
            break
    return tokens


## Beam search

def log_softmax(logits):
    logits = logits - np.max(logits)
    return logits - np.log(np.sum(np.exp(logits)))

def beam_search(model, start_token, eos_token, beam_width=3, max_len=20):
    # (tokens, cumuative_log_prob)
    beams = [([start_token], 0.0)]

    for _ in range(max_len):
        candidates = []
        for tokens, score in beams:

            # finished sequence
            if tokens[-1] == eos_token:
                candidates.append((tokens, score))
                continue

            logits = model(tokens)
            log_probs = log_softmax(logits)

            # expand all V tokens
            for token in range(len(log_probs)):
                new_tokens = tokens + [token]
                new_score = score + log_probs[token]

                candidates.append((new_tokens, new_score))

        candidates.sort(key=lambda x: x[1], reverse=True)
        beams = candidates[:beam_width]

        if all(tokens[-1] == eos_token for tokens,_ in beams):
            break
    return beams[0][0]
