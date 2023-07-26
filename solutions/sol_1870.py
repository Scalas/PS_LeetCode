from typing import List
from math import ceil


class Solution:
    @staticmethod
    def min_speed_on_time(dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1

        def check(speed):
            res = 0
            for num in dist[:-1]:
                res += ceil(num / speed)
            return hour - (res + dist[-1] / speed)

        s, e = 1, 10 ** 7
        while s < e:
            mid = (s + e) // 2
            c = check(mid)
            if c >= 0:
                e = mid
            elif c < 0:
                s = mid + 1
        return e
