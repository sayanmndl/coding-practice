

class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for j in range(len(s)+1):
            for i in range(j):
                if dp[i] and s[i:j] in words:
                    dp[j] = True
                    break
        return dp[len(s)]