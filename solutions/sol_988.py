from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def smallest_from_leaf(root: Optional[TreeNode]) -> str:
        string = []

        def dfs(cur, buf):
            buf.append(cur.val)
            is_leaf = True
            if cur.left:
                dfs(cur.left, buf)
                is_leaf = False
            if cur.right:
                dfs(cur.right, buf)
                is_leaf = False
            if is_leaf:
                string.append(buf[::-1])
            buf.pop()

        dfs(root, [])
        return "".join(map(lambda x: chr(x + ord("a")), min(string)))
