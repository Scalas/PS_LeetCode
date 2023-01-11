from typing import List


class Solution:
    @staticmethod
    def min_time(n: int, edges: List[List[int]], has_apple: List[bool]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n
        answer = 0

        def dfs(cur):
            nonlocal answer

            visited[cur] = True
            res = has_apple[cur]
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                if dfs(nxt):
                    answer += 2
                    res = True
            return res

        dfs(0)

        return answer
