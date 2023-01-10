from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(cur1, cur2):
            if not cur1 or not cur2:
                return cur1 == cur2
            if cur1.val != cur2.val:
                return False
            if not dfs(cur1.left, cur2.left):
                return False
            if not dfs(cur1.right, cur2.right):
                return False
            return True
        return dfs(p, q)
