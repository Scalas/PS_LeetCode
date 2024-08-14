from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    @staticmethod
    def smallest_distance_pair(nums: List[int], k: int) -> int:
        sn = sorted(nums)
        n = len(sn)

        def check(dist):
            lower, count = 0, 0
            for i in range(n):
                target = dist + sn[i]
                lo, hi = i + 1, n
                left = bisect_left(sn, target, lo, hi)
                right = bisect_right(sn, target, lo, hi)
                if left == right:
                    lower += left - lo
                else:
                    lower += left - lo
                    count += right - left
            if lower >= k:
                return 1
            if lower + count < k:
                return -1
            return 0

        s, e = 0, sn[-1] - sn[0]
        while s <= e:
            mid_dist = (s + e) // 2
            c = check(mid_dist)
            if c == -1:
                s = mid_dist + 1
            elif c == 1:
                e = mid_dist - 1
            else:
                return mid_dist
        return -1
