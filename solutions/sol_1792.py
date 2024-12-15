from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def max_average_ratio(classes: List[List[int]], extra_students: int) -> float:
        def delta(x, y):
            return (x - y) / (x * (x + 1))

        q = [[-delta(t, p), p, t] for p, t in classes]
        heapify(q)
        for _ in range(extra_students):
            _, passed, total = heappop(q)
            heappush(q, [-delta(total + 1, passed + 1), passed + 1, total + 1])

        return sum([p / t for _, p, t in q]) / len(q)
