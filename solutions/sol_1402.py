from bisect import bisect_right
from typing import List


class Solution:
    @staticmethod
    def max_satisfaction(satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()

        start = bisect_right(satisfaction, 0)
        cur = 0
        idx = 1
        for i in range(start, n):
            cur += (satisfaction[i] * idx)
            idx += 1

        for i in range(1, n):
            satisfaction[i] += satisfaction[i - 1]
        satisfaction.append(0)

        answer = cur
        total = satisfaction[n-1]
        for s in range(start - 1, -1, -1):
            cur += (total - satisfaction[s - 1])
            answer = max(answer, cur)
        return answer
