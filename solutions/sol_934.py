from typing import List


class Solution:
    @staticmethod
    def shortest_bridge(grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        marked = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q = [(i, j)]
                    grid[i][j] = 2
                    while q:
                        nq = []
                        for r, c in q:
                            for dr, dc in direction:
                                nr, nc = r + dr, c + dc
                                if not (0 <= nr < n and 0 <= nc < n):
                                    continue
                                if grid[nr][nc] != 1:
                                    continue
                                grid[nr][nc] = 2
                                nq.append((nr, nc))
                        q = nq
                    marked = True
                    break
            if marked:
                break

        q = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        bridge = -1
        while q:
            bridge += 1
            nq = []
            for r, c in q:
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == 2:
                        return bridge
                    if grid[nr][nc] == 1:
                        continue
                    grid[nr][nc] = 1
                    nq.append((nr, nc))
                q = nq
        return -1
