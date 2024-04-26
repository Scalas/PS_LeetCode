from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    @staticmethod
    def min_falling_path_sum(grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = [[grid[0][i], i] for i in range(m)]
        heapify(q)
        for i in range(1, n):
            nq = []
            for j in range(m):
                min_prev, idx = q[0]
                if j == idx:
                    tmp = heappop(q)
                    min_cur = q[0][0] + grid[i][j]
                    heappush(nq, [min_cur, j])
                    heappush(q, tmp)
                else:
                    min_cur = q[0][0] + grid[i][j]
                    heappush(nq, [min_cur, j])
            q = nq
        return min(q)[0]
