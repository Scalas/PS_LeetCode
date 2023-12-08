from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def tree2str(root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def dfs(cur):
            res = [str(cur.val)]
            if cur.left:
                res.append(f"({dfs(cur.left)})")
            if cur.right:
                if len(res) == 1:
                    res.append("()")
                res.append(f"({dfs(cur.right)})")
            return "".join(res)

        return dfs(root)
