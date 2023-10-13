from typing import List


class Solution:
    @staticmethod
    def min_cost_climbing_stairs(cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(n - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])
