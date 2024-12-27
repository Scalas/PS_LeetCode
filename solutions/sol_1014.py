from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def max_score_sightseeing_pair(values: List[int]) -> int:
        n = len(values)
        q = []
        for i in range(n):
            heappush(q, [i - values[i], i])
        removed = [False] * n
        res = 0
        for i in range(n - 1):
            score = values[i] + i
            removed[i] = True
            while removed[q[0][1]]:
                heappop(q)
            res = max(res, score - q[0][0])
        return res
