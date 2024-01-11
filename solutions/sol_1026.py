from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def max_ancestor_diff(root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(cur, minv, maxv):
            nminv = min(minv, cur.val)
            nmaxv = max(maxv, cur.val)
            res = nmaxv - nminv
            if cur.left:
                res = max(res, dfs(cur.left, nminv, nmaxv))
            if cur.right:
                res = max(res, dfs(cur.right, nminv, nmaxv))
            return res

        return dfs(root, 10**9, -1)
