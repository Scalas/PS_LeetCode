from typing import List


class Solution:
    @staticmethod
    def generate_matrix(n: int) -> List[List[int]]:
        answer = [[-1] * n for _ in range(n)]
        total = n**2
        r, c = 0, -1
        dr, dc = 0, 1
        num = 1
        while num <= total:
            while True:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n):
                    break
                if answer[nr][nc] != -1:
                    break
                answer[nr][nc] = num
                num += 1
                r, c = nr, nc
            dr, dc = dc, dr * (1 if dc else -1)
        return answer
