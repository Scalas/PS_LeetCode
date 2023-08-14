from typing import List


class Solution:
    @staticmethod
    def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        n = len(grid)
        if n == 1:
            return 1

        visited = [[False] * n for _ in range(n)]
        q = [(0, 0)]
        visited[0][0] = True
        turn = 1
        while q:
            turn += 1
            nq = []
            for cr, cc in q:
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == 1:
                        continue
                    if nr == nc == n - 1:
                        return turn
                    if visited[nr][nc]:
                        continue
                    visited[nr][nc] = True
                    nq.append((nr, nc))
            q = nq
        return -1
