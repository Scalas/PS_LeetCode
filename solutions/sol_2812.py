from typing import List


class Solution:
    @staticmethod
    def maximum_safeness_factor(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dist = [[-1] * m for _ in range(n)]

        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append([i, j])
        d = 0
        for cr, cc in q:
            dist[cr][cc] = 0
        while q:
            nq = []
            d += 1
            for cr, cc in q:
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if dist[nr][nc] != -1:
                        continue
                    dist[nr][nc] = d
                    nq.append([nr, nc])
            q = nq

        def is_reachable(factor):
            nonlocal n, m
            q = [[0, 0]]
            visited = [[False] * m for _ in range(n)]
            if dist[0][0] < factor:
                return False
            visited[0][0] = True
            while q:
                nq = []
                for r, c in q:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < n and 0 <= nc < m):
                            continue
                        if dist[nr][nc] < factor:
                            continue
                        if visited[nr][nc]:
                            continue
                        visited[nr][nc] = True
                        nq.append([nr, nc])
                q = nq
            return visited[n - 1][m - 1]

        s, e = 0, n + m - 1
        answer = 0
        while s <= e:
            mid = (s + e) // 2
            if is_reachable(mid):
                answer = max(answer, mid)
                s = mid + 1
            else:
                e = mid - 1
        return answer
