class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        def f(s, t, i, j, dp):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
                
            if s[i] == t[j]:
                dp[i][j] = f(s, t, i-1, j-1, dp) + f(s, t, i-1, j, dp)
                return dp[i][j]

            dp[i][j] = f(s, t, i-1, j, dp)
            return dp[i][j]
            
        return f(s, t, n - 1, m - 1, dp)