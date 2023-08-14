from typing import List


class Solution:
    @staticmethod
    def is_bipartite(graph: List[List[int]]) -> bool:
        n = len(graph)
        group = [-1] * n

        def dfs(cur, group_id):
            if group[cur] == group_id:
                return True
            if group[cur] == -1:
                group[cur] = group_id
                for nxt in graph[cur]:
                    if not dfs(nxt, 1 - group_id):
                        return False
                return True
            else:
                return False

        for i in range(n):
            if group[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
