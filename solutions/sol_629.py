class Solution:
    @staticmethod
    def k_inverse_pairs(n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[-1] * (k + 1) for _ in range(n + 1)]
        acc = [[0] * (k + 2) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
            acc[i][0] = 1
        for i in range(1, k + 1):
            dp[1][i] = 0
            acc[1][i] = 1

        for cur in range(2, n + 1):
            for inv in range(1, k + 1):
                low = inv - min(cur, inv + 1)
                res = acc[cur - 1][inv] - acc[cur - 1][low]
                dp[cur][inv] = res
                acc[cur][inv] = acc[cur][inv - 1] + res
        return dp[n][k] % mod
