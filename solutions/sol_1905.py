from typing import List


class Solution:
    @staticmethod
    def count_sub_islands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n, m = len(grid1), len(grid1[0])
        group = [[-1] * m for _ in range(n)]

        def grouping(sr, sc, gid):
            q = [[sr, sc]]
            group[sr][sc] = gid
            grid1[sr][sc] = 0
            while q:
                nq = []
                for cr, cc in q:
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if not (0 <= nr < n and 0 <= nc < m):
                            continue
                        if grid1[nr][nc] != 1:
                            continue
                        grid1[nr][nc] = 0
                        group[nr][nc] = gid
                        nq.append([nr, nc])
                q = nq

        def subisland(sr, sc):
            q = [[sr, sc]]
            gid = group[i][j]
            res = True
            while q:
                nq = []
                for cr, cc in q:
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if not (0 <= nr < n and 0 <= nc < m):
                            continue
                        if grid2[nr][nc] != 1:
                            continue
                        if group[nr][nc] != gid:
                            res = False
                        grid2[nr][nc] = 0
                        nq.append([nr, nc])
                q = nq
            return res

        group_id = 0
        for i in range(n):
            for j in range(m):
                if grid1[i][j] != 1:
                    continue
                grouping(i, j, group_id)
                group_id += 1

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] != 1 or group[i][j] == -1:
                    continue
                if subisland(i, j):
                    answer += 1
        return answer
