from typing import List
from heapq import heapify, heappush, heappop
from math import ceil


class Solution:
    @staticmethod
    def max_k_elements(nums: List[int], k: int) -> int:
        q = [-num for num in nums]
        heapify(q)
        score = 0
        for _ in range(k):
            num = -heappop(q)
            score += num
            heappush(q, -ceil(num / 3))
        return score
