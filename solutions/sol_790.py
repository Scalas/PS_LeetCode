class Solution:
    @staticmethod
    def num_tilings(n: int) -> int:
        mod = 10**9 + 7
        if n < 3:
            return 2**n - 2 ** (n - 1)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, n + 1):
            res = 0
            res += dp[i - 1] - dp[i - 3]
            res += dp[i - 3] * 2
            dp[i] = dp[i - 1] + res
        return (dp[n] - dp[n - 1]) % mod
