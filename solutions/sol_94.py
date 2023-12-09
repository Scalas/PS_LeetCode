from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        traversal = []

        def dfs(cur):
            if cur.left:
                dfs(cur.left)
            traversal.append(cur.val)
            if cur.right:
                dfs(cur.right)

        dfs(root)

        return traversal
