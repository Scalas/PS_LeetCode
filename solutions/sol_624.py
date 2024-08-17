from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def max_distance(arrays: List[List[int]]) -> int:
        n = len(arrays)
        minh, maxh = [], []
        for i in range(n):
            nums = arrays[i]
            heappush(minh, [nums[0], i])
            heappush(maxh, [-nums[-1], i])
        answer = 0
        backup = None
        for i in range(n):
            min_num, max_num = arrays[i][0], arrays[i][-1]
            if minh[0][1] == i:
                backup = heappop(minh)
            answer = max(answer, abs(max_num - minh[0][0]))
            if backup:
                heappush(minh, backup)
                backup = None
            if maxh[0][1] == i:
                backup = heappop(maxh)
            answer = max(answer, abs(min_num + maxh[0][0]))
            if backup:
                heappush(maxh, backup)
                backup = None
        return answer
