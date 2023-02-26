class Solution:
    @staticmethod
    def min_distance(word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0 or m == 0:
            return abs(n - m)
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if word1[0] != word2[0] else 0
        for i in range(1, n):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, m):
            if word1[0] == word2[i]:
                dp[0][i] = i
            else:
                dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]
