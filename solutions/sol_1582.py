from typing import List


class Solution:
    @staticmethod
    def num_special(mat: List[List[int]]) -> int:
        row_acc = list(map(sum, mat))
        col_acc = list(map(sum, zip(*mat)))

        n, m = len(mat), len(mat[0])
        answer = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and row_acc[i] == 1 and col_acc[j] == 1:
                    answer += 1
        return answer
