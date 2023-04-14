class Solution:
    @staticmethod
    def longest_palindrome_subseq(s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i < n - 1:
                dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1

        def dfs(l, r):
            if dp[l][r] == -1:
                if s[l] == s[r]:
                    dp[l][r] = dfs(l + 1, r - 1) + 2
                else:
                    dp[l][r] = max(dfs(l + 1, r), dfs(l, r - 1))
            return dp[l][r]

        return dfs(0, n - 1)
