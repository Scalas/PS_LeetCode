from typing import List


class Solution:

    @staticmethod
    def min_falling_path_sum(matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = matrix[0][:]
        for line in matrix[1:]:
            ndp = [0] * m
            for i in range(m):
                res = dp[i]
                if i > 0:
                    res = min(res, dp[i - 1])
                if i < m - 1:
                    res = min(res, dp[i + 1])
                ndp[i] = line[i] + res
            dp = ndp
        return min(dp)
