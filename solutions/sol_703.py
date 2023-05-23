from heapq import heappush, heappop, heapify
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        self.q = nums
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.q, val)
        if len(self.q) > self.k:
            heappop(self.q)
        return self.q[0]
