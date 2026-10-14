from collections import Counter
import heapq

def top_k_contributors(chat_log, k):
    counts = Counter()
    for sender, message in chat_log:
        counts[sender] += 1

    top_k = heapq.nlargest(k, counts.items(), key = lambda x: x[1])
    return top_k[::-1]