from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def min_cost_to_hire_workers(quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        r = [[wage[i] / quality[i], i] for i in range(n)]
        r.sort()

        qh = []
        qs = 0
        for i in range(k - 1):
            idx = r[i][1]
            q = quality[idx]
            heappush(qh, -q)
            qs += q

        answer = float("inf")
        for i in range(k - 1, n):
            rate, idx = r[i]
            q = quality[idx]
            heappush(qh, -q)
            qs += q
            if len(qh) > k:
                qs += heappop(qh)
            answer = min(answer, qs * rate)
        return answer
