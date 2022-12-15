class Solution:
    @staticmethod
    def longest_common_subsequence(text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        if n == 0 or m == 0:
            return 0
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1 if text1[i] == text2[0] else 0
            if i > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0])
        for i in range(m):
            dp[0][i] = 1 if text1[0] == text2[i] else 0
            if i > 0:
                dp[0][i] = max(dp[0][i], dp[0][i - 1])
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return max([max(dp[i]) for i in range(n)])
