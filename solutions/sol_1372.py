from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def longest_zig_zag(root: Optional[TreeNode]) -> int:
        dp = dict()
        idx = -1

        answer = 0

        def dfs(cur, d):
            nonlocal idx, answer

            if cur.val > 0:
                cur.val = idx
                idx -= 1
                left, right = 0, 0
                if cur.left:
                    left = dfs(cur.left, 1)
                if cur.right:
                    right = dfs(cur.right, 0)
                dp[cur.val] = left + 1, right + 1
                answer = max(answer, left + 1, right + 1)

            return dp[cur.val][d]

        return max(dfs(root, 0), dfs(root, 1), answer) - 1
