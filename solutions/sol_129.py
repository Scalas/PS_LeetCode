from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def sum_numbers(root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node, num):
            if not node.left and not node.right:
                return num
            res = 0
            if node.left:
                res += dfs(node.left, num * 10 + node.left.val)
            if node.right:
                res += dfs(node.right, num * 10 + node.right.val)
            return res

        return dfs(root, root.val)
