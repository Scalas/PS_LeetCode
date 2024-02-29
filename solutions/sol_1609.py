from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def is_even_odd_tree(root: Optional[TreeNode]) -> bool:
        q = [root]
        lv = 0
        INF = 10**9
        while q:
            pre = INF * (1 if lv % 2 else -1)
            nq = []
            for cur in q:
                v = cur.val
                t = lv % 2
                if v % 2 == t:
                    return False
                if (t and v >= pre) or (not t and v <= pre):
                    return False
                pre = v
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            q = nq
            lv += 1
        return True
