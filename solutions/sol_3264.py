from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def get_final_state(nums: List[int], k: int, multiplier: int) -> List[int]:
        q = [[nums[i], i] for i in range(len(nums))]
        heapify(q)
        for _ in range(k):
            num, idx = heappop(q)
            heappush(q, [num * multiplier, idx])
        return [num for num, _ in sorted(q, key=lambda x: x[1])]
