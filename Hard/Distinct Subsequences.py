class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp, dpPrev = [0] * (n+1), [0] * (n+1)
        dp[0] = dpPrev[0] = 1
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = dpPrev[j]
                if s[i-1] == t[j-1]:
                    dp[j] += dpPrev[j-1]
            dp, dpPrev = dpPrev, dp
        return dpPrev[n]