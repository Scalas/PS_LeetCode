from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def kth_largest_level_sum(root: Optional[TreeNode], k: int) -> int:
        levels = []
        q = [root]
        while q:
            nq = []
            ls = 0
            for cur in q:
                ls += cur.val
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            levels.append(ls)
            q = nq
        levels.sort()
        if len(levels) < k:
            return -1
        return levels[-k]
