from typing import List


class Solution:
    @staticmethod
    def paint_walls(cost: List[int], time: List[int]) -> int:
        n = len(cost)
        INF = float("inf")
        dp = [[-1] * 501 for _ in range(n)]

        def dfs(cur, remain):
            if remain <= 0:
                return 0
            if cur == n:
                return INF
            if dp[cur][remain] == -1:
                res1 = dfs(cur + 1, remain)
                res2 = dfs(cur + 1, remain - time[cur] - 1) + cost[cur]
                dp[cur][remain] = min(res1, res2)
            return dp[cur][remain]

        return dfs(0, n)
