class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        dp = [[None] * (m + 1) for _ in range(n + 1)]

        def dfs(i1, i2):
            i3 = i1 + i2
            if i3 == k:
                return i1 == n and i2 == m
            if dp[i1][i2] is None:
                if i1 < n and s1[i1] == s3[i3] and dfs(i1 + 1, i2):
                    dp[i1][i2] = True
                elif i2 < m and s2[i2] == s3[i3] and dfs(i1, i2 + 1):
                    dp[i1][i2] = True
                else:
                    dp[i1][i2] = False
            return dp[i1][i2]

        return dfs(0, 0)
