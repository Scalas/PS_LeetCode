from typing import List


class Solution:
    @staticmethod
    def update_matrix(mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(mat), len(mat[0])

        answer = [[-1] * m for _ in range(n)]
        q = [(i, j) for i in range(n) for j in range(m) if mat[i][j] == 0]
        for r, c in q:
            answer[r][c] = 0
        turn = 0
        while q:
            turn += 1
            nq = []
            for r, c in q:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if mat[nr][nc] == 0:
                        continue
                    if answer[nr][nc] != -1:
                        continue
                    answer[nr][nc] = turn
                    nq.append((nr, nc))
            q = nq
        return answer
