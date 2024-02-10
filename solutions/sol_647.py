class Solution:
    @staticmethod
    def count_substrings(s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            dp[i][i + 1] = 1 if s[i] == s[i + 1] else 0
        for g in range(2, n):
            for i in range(n - g):
                dp[i][i + g] = (
                    1 if dp[i + 1][i + g - 1] == 1 and s[i] == s[i + g] else 0
                )
        return sum([sum(line) for line in dp])
