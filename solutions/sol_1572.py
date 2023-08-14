from typing import List


class Solution:
    @staticmethod
    def diagonal_sum(mat: List[List[int]]) -> int:
        n = len(mat)
        answer = 0
        for i in range(n):
            answer += mat[i][i] + mat[i][n - 1 - i]
        if n % 2:
            mid = n // 2
            answer -= mat[mid][mid]
        return answer
