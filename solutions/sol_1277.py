from typing import List


class Solution:
    @staticmethod
    def count_squares(matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i < n - 1:
                    matrix[i + 1][j] += matrix[i][j]
                if j > 0:
                    matrix[i][j] += matrix[i][j - 1]
            matrix[i].append(0)
        matrix.append([0] * m)

        def count(side):
            nonlocal n, m
            target = side**2
            res = 0
            for i in range(n - side + 1):
                for j in range(m - side + 1):
                    s1 = matrix[i + side - 1][j + side - 1]
                    s2 = matrix[i + side - 1][j - 1]
                    s3 = matrix[i - 1][j + side - 1]
                    s4 = matrix[i - 1][j - 1]
                    if s1 - s2 - s3 + s4 == target:
                        res += 1
            return res

        answer = 0
        for i in range(1, max(n, m) + 1):
            answer += count(i)
        return answer
