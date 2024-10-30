from typing import List


class Solution:
    @staticmethod
    def max_moves(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        k = n * m
        g = [[] for _ in range(k)]
        directions = [[-1, 1], [0, 1], [1, 1]]
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if grid[nr][nc] > grid[i][j]:
                        g[idx].append(nr * m + nc)

        def dfs(cur):
            nonlocal k, depth
            if cur == k:
                return 0
            if depth[cur] == -1:
                res = 0
                for nxt in g[cur]:
                    res = max(res, dfs(nxt) + 1)
                depth[cur] = res
            return depth[cur]

        depth = [-1] * k
        for i in range(0, k, m):
            dfs(i)
        return max(depth)
