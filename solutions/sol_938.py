from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(cur):
            res = 0
            if cur.left:
                res += dfs(cur.left)
            if cur.right:
                res += dfs(cur.right)
            if low <= cur.val <= high:
                res += cur.val
            return res

        return dfs(root)
