from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def max_depth(root: Optional[TreeNode]) -> int:
        q = [root]
        depth = 0
        while q:
            depth += 1
            nq = []
            for cur in q:
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            q = nq
        return depth
