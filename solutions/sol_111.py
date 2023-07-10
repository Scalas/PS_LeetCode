from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def min_depth(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            depth += 1
            nq = []
            for cur in q:
                is_leaf = True
                if cur.left:
                    nq.append(cur.left)
                    is_leaf = False
                if cur.right:
                    nq.append(cur.right)
                    is_leaf = False
                if is_leaf:
                    return depth
            q = nq
        return depth
