from typing import List


class Solution:
    @staticmethod
    def lucky_numbers(matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        col = list(map(max, zip(*matrix)))
        row = list(map(min, matrix))
        answer = []
        for i in range(n):
            for j in range(m):
                if row[i] == col[j]:
                    answer.append(matrix[i][j])
        return answer
