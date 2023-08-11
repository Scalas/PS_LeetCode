from typing import List


class Solution:
    @staticmethod
    def change(amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount
        dp = [[-1] * (m + 1) for _ in range(n)]

        def dfs(cur, remain):
            if cur == n - 1:
                return 0 if remain % coins[cur] else 1
            if dp[cur][remain] == -1:
                coin = coins[cur]
                res = 0
                for i in range(remain // coin + 1):
                    res += dfs(cur + 1, remain - coin * i)
                dp[cur][remain] = res
            return dp[cur][remain]
        return dfs(0, amount)
