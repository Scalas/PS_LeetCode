class Solution:
    @staticmethod
    def min_steps(n: int) -> int:
        dp = [0, 0]
        for i in range(2, n + 1):
            res = i
            for j in range(2, i // 2 + 1):
                if i % j:
                    continue
                res = min(res, dp[j] + i // j)
            dp.append(res)
        return dp[n]
