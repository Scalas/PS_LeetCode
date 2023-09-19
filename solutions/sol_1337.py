from typing import List


class Solution:
    @staticmethod
    def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
        n = len(mat[0])
        answer = []
        for i in range(len(mat)):
            check = False
            for j in range(n):
                if mat[i][j] == 0:
                    answer.append((j, i))
                    check = True
                    break
            if not check:
                answer.append((n, i))
        answer.sort()
        return [j for i, j in answer][:k]
