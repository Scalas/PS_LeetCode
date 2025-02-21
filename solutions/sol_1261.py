from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        s = set()

        def dfs(cur, v):
            nonlocal s
            s.add(v)
            cur.val = v
            if cur.left:
                dfs(cur.left, v * 2 + 1)
            if cur.right:
                dfs(cur.right, v * 2 + 2)

        dfs(root, 0)
        self.s = s

    def find(self, target: int) -> bool:
        return target in self.s
