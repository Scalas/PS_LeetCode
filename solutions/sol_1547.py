from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    @staticmethod
    def min_cost(n: int, cuts: List[int]) -> int:
        cuts.sort()
        dp = dict()

        def cost(s, e):
            if (s, e) not in dp:
                left = bisect_left(cuts, s + 1)
                right = bisect_right(cuts, e - 1) - 1
                if left > right:
                    return 0
                if left == right:
                    return e - s
                res = 10 ** 9
                for m in range(left, right + 1):
                    res = min(res, cost(s, cuts[m]) + cost(cuts[m], e) + e - s)
                dp[(s, e)] = res
            return dp[(s, e)]

        return cost(0, n)
