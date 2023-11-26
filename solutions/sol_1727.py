from typing import List


class Solution:
    @staticmethod
    def largest_sub_matrix(matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    dp[i][j] = 1
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

        answer = 0
        for i in range(n):
            line = dp[i]
            line.sort(reverse=True)
            for j in range(m):
                answer = max(answer, dp[i][j] * (j + 1))
        return answer
