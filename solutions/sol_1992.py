from typing import List


class Solution:
    @staticmethod
    def find_farmland(land: List[List[int]]) -> List[List[int]]:
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(land), len(land[0])

        def bfs(sr, sc):
            q = [[sr, sc]]
            while q:
                nq = []
                for cr, cc in q:
                    for dr, dc in direction:
                        nr, nc = cr + dr, cc + dc
                        if not (0 <= nr < n and 0 <= nc < m):
                            continue
                        if land[nr][nc] == 0:
                            continue
                        land[nr][nc] = 0
                        nq.append([nr, nc])
                if not nq:
                    return q[0]
                q = nq

        answer = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    land[i][j] = 0
                    er, ec = bfs(i, j)
                    answer.append([i, j, er, ec])
        return answer
