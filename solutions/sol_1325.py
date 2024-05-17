from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def remove_leaf_nodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(cur):
            is_leaf = True
            if cur.left:
                if dfs(cur.left):
                    is_leaf = False
                else:
                    cur.left = None
            if cur.right:
                if dfs(cur.right):
                    is_leaf = False
                else:
                    cur.right = None
            if is_leaf:
                return cur.val != target
            return True

        return root if dfs(root) else None
