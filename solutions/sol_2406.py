from typing import List


class Solution:
    @staticmethod
    def min_groups(intervals: List[List[int]]) -> int:
        acc = [0] * (10**6 + 2)
        for u, v in intervals:
            acc[u] += 1
            acc[v + 1] -= 1
        answer = acc[0]
        for i in range(1, len(acc)):
            acc[i] += acc[i - 1]
            answer = max(answer, acc[i])
        return answer
