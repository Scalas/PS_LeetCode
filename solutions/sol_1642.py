from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pre = 0
        q = []
        s = 0
        for i in range(1, n):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                continue
            heappush(q, diff)
            s += diff
            if len(q) > ladders:
                s -= heappop(q)
            if pre + diff - s > bricks:
                return i - 1
            pre += diff
        return n - 1
