from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def evaluate_tree(root: Optional[TreeNode]) -> bool:
        def eval_tree(cur):
            if cur.val <= 1:
                return cur.val == 1
            left = eval_tree(cur.left)
            right = eval_tree(cur.right)
            if cur.val == 2:
                return left or right
            else:
                return left and right

        return eval_tree(root)
