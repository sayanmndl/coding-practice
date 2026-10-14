from collections import defaultdict


class Solution:
    def largestWordCount(
        self, messages, senders
        ):

        counts = defaultdict(int)
        for messge, sender in zip(messages, senders):
            counts[sender] += len(messages.split())
        
        best_sender = ""

        for sender in counts:
            if (
                best_sender == "" or counts[sender] > counts[best_sender]
                or (
                    counts[sender] == counts[best_sender] and sender > best_sender
                )
            ):
                best_sender = sender

        return best_sender