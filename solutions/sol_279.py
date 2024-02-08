class Solution:
    @staticmethod
    def num_squares(n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            res = i
            for r in range(1, int(i**0.5) + 1):
                res = min(res, dp[i - r**2] + 1)
            dp[i] = res
        return dp[n]
