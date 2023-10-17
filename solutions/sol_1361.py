from typing import List


class Solution:
    @staticmethod
    def validate_binary_tree_nodes(
        n: int, left_child: List[int], right_child: List[int]
    ) -> bool:
        g = [[left_child[i], right_child[i]] for i in range(n)]
        degree = [0] * n
        for u, v in g:
            if u != -1:
                degree[u] += 1
            if v != -1:
                degree[v] += 1
        root = [i for i in range(n) if not degree[i]]

        # exactly one root of tree should given
        if len(root) != 1:
            return False

        visited = [False] * n

        def dfs(cur):
            visited[cur] = True
            for nxt in g[cur]:
                if nxt == -1:
                    continue
                if visited[nxt]:
                    return False
                if not dfs(nxt):
                    return False
            return True

        # all nodes should be connected
        if not dfs(root[0]):
            return False

        for visit in visited:
            if not visit:
                return False

        return True
