class Solution:
    def maxProfit(self, weights, profits, capacity):
        dp = [0]*(capacity+1)

        for w, p in zip(weights, profits):
            for c in range(capacity, w-1,-1):
                dp[c] = max(
                    dp[c], dp[c-w]+p
                )

        return dp[capacity]


class Solution:
    def maxProfit(self, weights, profits, capacity):
        scale = 100

        int_weights = [
            int(round(w*scale)) for w in weights
        ]

        int_capacity = int(round(capacity*scale))

        dp = [0]*(int_capacity+1)
        for w, profit in zip(int_weights,profits):
            for c in range(int_capacity, w-1,-1):
                dp[c] = max(
                    dp[c], dp[c-w]+profit
                )

        return dp[int_capacity]