from typing import List


class Solution:
    @staticmethod
    def max_distance(grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j))
        if len(q) == n ** 2:
            return -1
        answer = -1
        while q:
            answer += 1
            nq = []
            for ci, cj in q:
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if not (0 <= ni < n and 0 <= nj < n):
                        continue
                    if visited[ni][nj]:
                        continue
                    if grid[ni][nj]:
                        continue
                    visited[ni][nj] = True
                    nq.append((ni, nj))
            q = nq
        return answer
