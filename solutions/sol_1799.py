from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def max_score(nums: List[int]) -> int:
        n = len(nums)
        m = n // 2
        bit = [1 << i for i in range(n)]
        full_visit = (1 << n) - 1
        gcd_mem = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                x, y = nums[i], nums[j]
                if x < y:
                    x, y = y, x
                while y:
                    x, y = y, x % y
                gcd_mem[i][j] = x

        dp = defaultdict(int)

        def dfs(cur, visit):
            if visit == full_visit:
                return 0
            if visit not in dp:
                res = 0
                for s in range(n):
                    for e in range(s + 1, n):
                        if visit & bit[s] or visit & bit[e]:
                            continue
                        nvisit = visit | bit[s] | bit[e]
                        res = max(res, dfs(cur + 1, nvisit) + cur * gcd_mem[s][e])
                dp[visit] = res
            return dp[visit]
        return dfs(1, 0)
