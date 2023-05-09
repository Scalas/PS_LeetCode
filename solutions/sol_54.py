from typing import List


class Solution:
    @staticmethod
    def spiral_order(matrix: List[List[int]]) -> List[int]:
        answer = []
        n, m = len(matrix), len(matrix[0])
        vc = 0
        total = n * m
        r, c = 0, -1
        dr, dc = 0, 1
        while vc < total:
            while True:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    break
                if matrix[nr][nc] == 101:
                    break
                answer.append(matrix[nr][nc])
                matrix[nr][nc] = 101
                vc += 1
                r, c = nr, nc
            dr, dc = dc, dr * (1 if dc else -1)
        return answer
