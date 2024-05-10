from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def kth_smallest_prime_fraction(arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = []
        for i in range(n):
            heappush(q, [arr[0] / arr[i], 0, i])

        res = [-1, -1]
        for _ in range(k):
            _, u, d = heappop(q)
            res = [arr[u], arr[d]]
            heappush(q, [arr[u + 1] / arr[d], u + 1, d])
        return res
