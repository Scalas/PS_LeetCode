from typing import List


class Solution:
    @staticmethod
    def find_circle_num(is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if is_connected[i][j]:
                    g[i].append(j)
                    g[j].append(i)

        def dfs(cur):
            visited[cur] = True
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                dfs(nxt)

        answer = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                dfs(i)
                answer += 1

        return answer
