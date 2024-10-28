from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def tree_queries(root: Optional[TreeNode], queries: List[int]) -> List[int]:
        md = dict()
        g = defaultdict(list)

        def dfs(cur, d):
            depth = d
            if cur.left:
                g[cur.val].append(cur.left.val)
                depth = max(depth, dfs(cur.left, d + 1))
            if cur.right:
                g[cur.val].append(cur.right.val)
                depth = max(depth, dfs(cur.right, d + 1))
            md[cur.val] = depth
            return depth

        dfs(root, 0)

        wd = dict()
        q = [root.val]
        bd = -1
        while q:
            nq = []
            max_depth = [[-md[i], i] for i in q]
            heapify(max_depth)
            for cur in q:
                for nxt in g[cur]:
                    nq.append(nxt)
                if max_depth[0][1] == cur:
                    v = heappop(max_depth)
                    wd[cur] = -max_depth[0][0] if max_depth else max(bd, 0)
                    heappush(max_depth, v)
                else:
                    wd[cur] = -max_depth[0][0]
            q = nq
            bd += 1

        return [wd[query] for query in queries]
