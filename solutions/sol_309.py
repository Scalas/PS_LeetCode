from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        n = len(prices)
        dp = [-1] * n

        def dfs(cur):
            if cur >= n:
                return 0
            if dp[cur] < 0:
                res = 0
                # 사지 않을 경우
                res = max(res, dfs(cur + 1))

                # 살 경우
                for sell_at in range(cur + 1, n):
                    res = max(res, dfs(sell_at + 2) + prices[sell_at] - prices[cur])
                dp[cur] = res
            return dp[cur]

        return dfs(0)
