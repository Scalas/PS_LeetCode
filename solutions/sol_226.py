from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverse(cur):
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                inverse(cur.left)
            if cur.right:
                inverse(cur.right)
        if root:
            inverse(root)
        return root
