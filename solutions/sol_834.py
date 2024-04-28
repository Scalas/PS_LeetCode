from typing import List


class Solution:
    @staticmethod
    def sum_of_distances_in_tree(n: int, edges: List[List[int]]) -> List[int]:
        g: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        answer = [0] * n
        child_cnt = [0] * n

        def dfs(cur, depth):
            nonlocal root, visited
            answer[root] += depth
            visited[cur] = True
            child = 0
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                child += dfs(nxt, depth + 1) + 1
            child_cnt[cur] = child
            return child

        def dfs2(cur, parent):
            nonlocal visited
            visited[cur] = True
            child = child_cnt[cur]
            non_child = n - child - 1
            answer[cur] = parent + non_child - child - 1
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                dfs2(nxt, answer[cur])

        root = 0
        visited = [False] * n
        dfs(root, 0)
        visited = [False] * n
        visited[0] = True
        for c in g[root]:
            dfs2(c, answer[root])
        return answer
