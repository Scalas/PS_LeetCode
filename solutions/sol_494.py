from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_target_sum_ways(nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(cur, s):
            nonlocal n
            if cur == n:
                if s == target:
                    return 1
                return 0
            if s not in dp[cur]:
                dp[cur][s] = dfs(cur + 1, s + nums[cur]) + dfs(cur + 1, s - nums[cur])
            return dp[cur][s]

        dp = [defaultdict(int) for _ in range(n)]
        return dfs(0, 0)
