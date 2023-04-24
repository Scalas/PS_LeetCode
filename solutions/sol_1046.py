from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    @staticmethod
    def last_stone_weight(stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)
        while len(stones) > 1:
            heappush(stones, heappop(stones) - heappop(stones))
        return -stones[0]
