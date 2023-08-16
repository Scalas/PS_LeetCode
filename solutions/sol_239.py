from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        n = len(nums)
        removed = [False] * n

        q = []
        for i in range(k):
            heappush(q, (-nums[i], i))

        answer = [-q[0][0]]
        for i in range(k, n):
            removed[i - k] = True
            heappush(q, (-nums[i], i))
            while removed[q[0][1]]:
                heappop(q)
            answer.append(-q[0][0])
        return answer
