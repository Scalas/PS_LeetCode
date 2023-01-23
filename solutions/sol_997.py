from typing import List


class Solution:
    @staticmethod
    def find_judge(n: int, trust: List[List[int]]) -> int:
        degree = [0] * n
        for u, v in trust:
            degree[u - 1] -= 1
            degree[v - 1] += 1
        for i in range(n):
            if degree[i] == n - 1:
                return i + 1
        return -1
