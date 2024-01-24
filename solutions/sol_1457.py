from collections import defaultdict
from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def pseudo_palindromic_paths(root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def check(p):
            oc = 0
            for cnt in p.values():
                if cnt % 2:
                    oc += 1
            return oc <= 1

        def dfs(cur, path):
            is_leaf = True
            path[cur.val] += 1
            res = 0
            if cur.left:
                res += dfs(cur.left, path)
                is_leaf = False
            if cur.right:
                res += dfs(cur.right, path)
                is_leaf = False
            if is_leaf:
                res = 1 if check(path) else 0
            path[cur.val] -= 1
            return res

        return dfs(root, defaultdict(int))
