from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def min_diff_in_bst(root: Optional[TreeNode]) -> int:
        q = []
        answer = 10**9

        def dfs(cur):
            nonlocal answer
            if cur.left:
                dfs(cur.left)
            if q:
                answer = min(answer, cur.val - q.pop())
            q.append(cur.val)
            if cur.right:
                dfs(cur.right)

        dfs(root)
        return answer
