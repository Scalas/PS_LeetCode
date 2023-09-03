class Solution:
    @staticmethod
    def unique_paths(m: int, n: int) -> int:
        n, m = m, n
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        for d in range(1, n + m - 1):
            for i in range(n):
                if i + m - 1 < d:
                    continue
                j = d - i
                if j < 0:
                    continue
                res = 0
                if i > 0:
                    res += dp[i - 1][j]
                if j > 0:
                    res += dp[i][j - 1]
                dp[i][j] = res
        return dp[n - 1][m - 1]
