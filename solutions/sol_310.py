from collections import defaultdict
from typing import List
from heapq import heappush, heappop


class Solution:
    @staticmethod
    def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        node_down_height = [defaultdict(int) for _ in range(n)]

        def dfs(cur):
            visited[cur] = True
            res = 0
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                h = dfs(nxt) + 1
                node_down_height[cur][nxt] = h
                res = max(res, h)
            return res

        node_height = [-1] * n

        def dfs2(cur, h):
            visited[cur] = True
            q = [-h]
            for nxt in g[cur]:
                heappush(q, -node_down_height[cur][nxt])
            node_height[cur] = -q[0]
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                mh = -q[0]
                if node_down_height[cur][nxt] == mh:
                    heappop(q)
                    dfs2(nxt, -q[0] + 1)
                    heappush(q, -mh)
                else:
                    dfs2(nxt, mh + 1)

        visited = [False] * n
        dfs(0)
        visited = [False] * n
        dfs2(0, 0)
        min_height = min(node_height)
        return [node for node in range(n) if node_height[node] == min_height]
