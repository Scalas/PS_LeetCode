from typing import List


class Solution:
    @staticmethod
    def min_path_sum(grid: List[List[int]]) -> int:
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                pre = grid[i - 1][j]
                if j > 0:
                    pre = min(pre, grid[i][j - 1])
                grid[i][j] += pre

        return grid[-1][-1]
