from heapq import heapify, heappush, heappop
from math import floor, sqrt
from typing import List


class Solution:
    @staticmethod
    def pick_gifts(gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapify(gifts)
        for _ in range(k):
            heappush(gifts, -floor(sqrt(-heappop(gifts))))
        return -sum(gifts)
