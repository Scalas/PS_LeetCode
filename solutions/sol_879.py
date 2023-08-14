from typing import List


class Solution:
    @staticmethod
    def profitable_schemes(
        n: int, min_profit: int, group: List[int], profit: List[int]
    ) -> int:
        m = len(group)
        dp = [[[-1] * (min_profit + 1) for _ in range(n + 1)] for _ in range(m)]
        mod = 10**9 + 7

        def dfs(cur, remain, tp):
            if cur == m:
                return 0 if tp else 1
            if dp[cur][remain][tp] == -1:
                res = 0
                p = profit[cur]
                if remain >= group[cur]:
                    nremain = remain - group[cur]
                    if tp == min_profit:
                        for i in range(max(0, min_profit - p), min_profit + 1):
                            res = (res + dfs(cur + 1, nremain, i)) % mod
                    elif tp >= p:
                        res = (res + dfs(cur + 1, nremain, tp - p)) % mod
                res = (res + dfs(cur + 1, remain, tp)) % mod
                dp[cur][remain][tp] = res
            return dp[cur][remain][tp]

        return dfs(0, n, min_profit)
