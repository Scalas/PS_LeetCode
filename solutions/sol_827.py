from collections import defaultdict
from typing import List, Dict


class Solution:
    @staticmethod
    def largest_is_land(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        gid = 2
        gs: Dict[int, int] = defaultdict(int)
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                q = [[i, j]]
                grid[i][j] = gid
                size = 1
                while q:
                    nq = []
                    for cr, cc in q:
                        for dr, dc in directions:
                            nr, nc = cr + dr, cc + dc
                            if not (0 <= nr < n and 0 <= nc < m):
                                continue
                            if grid[nr][nc] != 1:
                                continue
                            grid[nr][nc] = gid
                            nq.append([nr, nc])
                            size += 1
                    q = nq
                gs[gid] = size
                gid += 1

        answer = max(gs.values()) if gs.values() else 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                size = 1
                adj = set()
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    gid = grid[nr][nc]
                    if gid not in adj:
                        adj.add(gid)
                        size += gs[gid]
                answer = max(answer, size)
        return answer
