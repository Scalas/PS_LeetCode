from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def candy(ratings: List[int]) -> int:
        n = len(ratings)

        qs = defaultdict(list)
        for i in range(n):
            qs[ratings[i]].append(i)

        qs = sorted(qs.items())
        candies = [-1] * n
        for r, q in qs:
            for cur in q:
                res = 1
                if cur > 0 and ratings[cur - 1] < r:
                    res = max(res, candies[cur - 1] + 1)
                if cur < n - 1 and ratings[cur + 1] < r:
                    res = max(res, candies[cur + 1] + 1)
                candies[cur] = res

        return sum(candies)
