from heapq import heappush
from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = [-1] * n
        dp[-1] = 0
        q = [-prices[-2], -prices[-1]]
        q.sort()
        for i in range(n - 2, -1, -1):
            res = dp[i + 1]
            res = max(res, -q[0] - prices[i] - fee)
            if i > 0:
                heappush(q, -res - prices[i - 1])
            dp[i] = res
        return max(dp)
