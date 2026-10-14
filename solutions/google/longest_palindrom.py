

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        st, longest = 0, 1
        for j in range(n):
            for i in range(j-1,-1,-1):
                if s[i] == s[j]:
                    if j-i+1==2 or dp[i+1][j-1]:
                        dp[i][j] = True

                        curr_len = j-i+1
                        if curr_len > longest:
                            st = i
                            longest = curr_len

        return s[st:st+longest]