from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        answer = 0
        n = len(height)
        q = []
        for i in range(n):
            heappush(q, (-height[i], i))
        removed = [False] * n
        ph = [(0, 10**9)]
        for i in range(n):
            h = height[i]
            removed[i] = True
            while q and removed[q[0][1]]:
                heappop(q)
            if q:
                wh, widx = min(h, -q[0][0]), q[0][1]
                heappush(ph, (-wh, widx))
            while ph and ph[0][1] <= i:
                heappop(ph)
            answer += max(0, -ph[0][0] - h)
        return answer
