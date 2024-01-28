from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def num_submatrix_sum_target(matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i < n - 1:
                    matrix[i + 1][j] += matrix[i][j]
                if j > 0:
                    matrix[i][j] += matrix[i][j - 1]
        for i in range(n):
            matrix[i].append(0)
        matrix.append([0] * (m + 1))

        answer = 0
        for i in range(m):
            for j in range(i, m):
                acc = [matrix[k][j] - matrix[k][i - 1] for k in range(n)]
                pre = defaultdict(int)
                pre[0] = 1
                for k in range(n):
                    need = acc[k] - target
                    answer += pre[need]
                    pre[acc[k]] += 1
        return answer
