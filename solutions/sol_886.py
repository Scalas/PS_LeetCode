from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def possible_bi_partition(n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]

        for u, v in dislikes:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        color = [-1] * n

        def dfs(cur, parent, cur_color):
            color[cur] = cur_color
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                if color[nxt] == cur_color:
                    return False
                if color[nxt] == -1:
                    dfs(nxt, cur, 1 - cur_color)
            return True

        for i in range(n):
            if color[i] != -1:
                continue
            if not dfs(i, -1, 0):
                return False
        return True
