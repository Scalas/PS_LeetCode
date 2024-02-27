from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(cur, depth):
            nonlocal answer
            left, right = 0, 0
            if cur.left:
                left = dfs(cur.left, depth + 1) + 1
            if cur.right:
                right = dfs(cur.right, depth + 1) + 1
            answer = max(answer, left + right)
            return max(left, right)

        dfs(root, 0)
        return answer
