from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def is_symmetric(root: Optional[TreeNode]) -> bool:
        def compare_tree(t1: Optional[TreeNode], t2: Optional[TreeNode]):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            if not compare_tree(t1.left, t2.right):
                return False
            if not compare_tree(t1.right, t2.left):
                return False
            return True

        return compare_tree(root.left, root.right)
