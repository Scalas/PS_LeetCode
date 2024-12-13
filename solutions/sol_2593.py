from heapq import heapify, heappop
from typing import List


class Solution:
    @staticmethod
    def find_score(nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        q = [[nums[i], i] for i in range(n)]
        heapify(q)

        score = 0
        while q:
            while q and marked[q[0][1]]:
                heappop(q)
            if q:
                num, idx = heappop(q)
                score += num
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < n - 1:
                    marked[idx + 1] = True
        return score
