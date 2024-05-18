from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def distribute_coins(root: Optional[TreeNode]) -> int:
        def dfs(cur):
            coin, move = cur.val - 1, 0
            if cur.left:
                c, m = dfs(cur.left)
                coin += c
                move += abs(c) + m
            if cur.right:
                c, m = dfs(cur.right)
                coin += c
                move += abs(c) + m
            return coin, move

        return dfs(root)[1]
