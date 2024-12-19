from heapq import heappush
from typing import List


class Solution:
    @staticmethod
    def max_chunks_to_sorted(arr: List[int]) -> int:
        n = len(arr)
        minq, maxq, start = [], [], 0
        answer = 0
        for i in range(n):
            num = arr[i]
            heappush(minq, num)
            heappush(maxq, -num)

            if minq[0] == start and -maxq[0] == i:
                answer += 1
                minq, maxq, start = [], [], i + 1
        return answer
