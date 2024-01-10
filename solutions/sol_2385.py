from collections import defaultdict
from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def amount_of_time(root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

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

        q = [start]
        answer = -1
        visited = {start}
        while q:
            answer += 1
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    nq.append(nxt)
            q = nq
        return answer
