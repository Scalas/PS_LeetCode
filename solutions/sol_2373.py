from typing import List


class Solution:
    @staticmethod
    def largest_local(grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n - 2
        res = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                r = 0
                for x in range(3):
                    for y in range(3):
                        r = max(r, grid[i + x][j + y])
                res[i][j] = r
        return res
