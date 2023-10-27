class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            if i < n - 1:
                dp[i][i + 1] = s[i] == s[i + 1]

        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        for d in range(n - 1, -1, -1):
            for i in range(n - d):
                j = i + d
                if dp[i][j]:
                    return s[i : j + 1]
