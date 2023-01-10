from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
        path = []

        def dfs(cur):
            if cur is None:
                return
            path.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)

        dfs(root)
        return path
