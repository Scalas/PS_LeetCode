from typing import List
from heapq import heappush, heappop


class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        cnd = [(0, nums[0])]
        for i in range(1, n):
            while cnd[0][1] < i:
                heappop(cnd)
            min_hop = cnd[0][0] + 1
            dp[i] = min_hop
            heappush(cnd, (min_hop, i + nums[i]))
        return dp[-1]
