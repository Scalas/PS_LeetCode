from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
        answer = []

        def dfs(cur):
            nonlocal answer
            if cur.left:
                dfs(cur.left)
            if cur.right:
                dfs(cur.right)
            answer.append(cur.val)

        if root:
            dfs(root)
        return answer
