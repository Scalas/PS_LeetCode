from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def longest_path(parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        roots = [0]
        for child_node in range(1, n):
            parent_node = parent[child_node]
            if s[child_node] != s[parent_node]:
                g[parent_node].append(child_node)
            else:
                roots.append(child_node)

        answer = 0

        def dfs(cur, depth):
            nonlocal answer
            path = []
            res = depth
            for nxt in g[cur]:
                max_depth = dfs(nxt, depth + 1)
                heappush(path, depth - max_depth)
                res = max(res, max_depth)
            count = 2
            length = 1
            while path and count:
                length -= heappop(path)
                count -= 1
            answer = max(answer, length)
            return res

        for root in roots:
            dfs(root, 0)

        return answer
