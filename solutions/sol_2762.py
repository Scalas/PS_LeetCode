from heapq import heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def continuous_sub_arrays(nums: List[int]) -> int:
        n = len(nums)
        minq, maxq = [], []
        out = 0
        removed = [False] * n
        answer = 0
        for cur in range(n):
            heappush(maxq, [-nums[cur], cur])
            heappush(minq, [nums[cur], cur])
            while -maxq[0][0] - minq[0][0] > 2:
                removed[out] = True
                out += 1
                while removed[maxq[0][1]]:
                    heappop(maxq)
                while removed[minq[0][1]]:
                    heappop(minq)
            answer += cur - out + 1
        return answer
