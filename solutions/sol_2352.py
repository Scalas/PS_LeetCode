from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def equal_pairs(grid: List[List[int]]) -> int:
        n = len(grid)
        count = defaultdict(int)
        for i in range(n):
            arr = []
            for j in range(n):
                arr.append(grid[i][j])
            count['_'.join(map(str, arr))] += 1

        answer = 0
        for i in range(n):
            arr = []
            for j in range(n):
                arr.append(grid[j][i])
            answer += count['_'.join(map(str, arr))]
        return answer
