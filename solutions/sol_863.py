from typing import List
from collections import defaultdict

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def distance_k(root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)

        def dfs(cur):
            if cur.left:
                g[cur.val].append(cur.left.val)
                g[cur.left.val].append(cur.val)
                dfs(cur.left)
            if cur.right:
                g[cur.val].append(cur.right.val)
                g[cur.right.val].append(cur.val)
                dfs(cur.right)

        dfs(root)

        q = [target.val]
        visited = defaultdict(bool)
        visited[target.val] = True
        for _ in range(k):
            if not q:
                return []
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq
        return q
