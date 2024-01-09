from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        t1, t2 = [], []

        def dfs(cur, t):
            is_leaf = True
            if cur.left:
                is_leaf = False
                dfs(cur.left, t)
            if cur.right:
                is_leaf = False
                dfs(cur.right, t)
            if is_leaf:
                t.append(cur.val)

        dfs(root1, t1)
        dfs(root2, t2)

        return t1 == t2
