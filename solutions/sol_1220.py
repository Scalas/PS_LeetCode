class Solution:
    @staticmethod
    def count_vowel_permutation(n: int) -> int:
        dp = [1] * 5
        mod = 10**9 + 7
        for _ in range(n - 1):
            ndp = [0] * 5
            ndp[0] = (dp[1] + dp[2] + dp[4]) % mod
            ndp[1] = (dp[0] + dp[2]) % mod
            ndp[2] = (dp[1] + dp[3]) % mod
            ndp[3] = dp[2]
            ndp[4] = (dp[2] + dp[3]) % mod
            dp = ndp
        return sum(dp) % mod
