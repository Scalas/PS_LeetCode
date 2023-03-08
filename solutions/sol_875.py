import math
from typing import List


class Solution:
    @staticmethod
    def min_eating_speed(piles: List[int], h: int) -> int:
        s, e = 1, max(piles)

        def check(k):
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            return time <= h

        while s < e:
            mid = (s + e) // 2
            if check(mid):
                e = mid
            else:
                s = mid + 1
        return e
