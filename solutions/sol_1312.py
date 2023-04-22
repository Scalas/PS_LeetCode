class Solution:
    @staticmethod
    def min_insertions(s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            if i < n - 1:
                dp[i][i + 1] = 1 if s[i] != s[i + 1] else 0

        def dfs(l, r):
            if dp[l][r] == -1:
                res = r - l
                if s[l] == s[r]:
                    res = min(res, dfs(l + 1, r - 1))
                else:
                    res = min(res, dfs(l + 1, r) + 1, dfs(l, r - 1) + 1)
                dp[l][r] = res
            return dp[l][r]

        return dfs(0, n - 1)
