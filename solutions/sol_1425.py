from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def constrained_subset_sum(nums: List[int], k: int) -> int:
        mv = max(nums)
        if mv <= 0:
            return mv

        kw = []
        n = len(nums)
        dp = [-1] * n
        for i in range(n):
            dp[i] = nums[i]
            while kw and i - kw[0][1] > k:
                heappop(kw)
            if kw:
                mp = -kw[0][0]
                if mp > 0:
                    dp[i] += mp
            heappush(kw, (-dp[i], i))
        return max(dp)
