from typing import List


class Solution:
    @staticmethod
    def ones_minus_zeros(grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        row_acc = list(map(sum, grid))
        col_acc = list(map(sum, zip(*grid)))
        return [
            [row_acc[i] * 2 - n + col_acc[j] * 2 - m for j in range(m)]
            for i in range(n)
        ]
