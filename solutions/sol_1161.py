from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def max_level_sum(root: Optional[TreeNode]) -> int:
        q = [root]
        answer, max_sum = 0, -10 ** 9
        level = 0
        while q:
            level += 1
            s = 0
            nq = []
            for cur in q:
                s += cur.val
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            if s > max_sum:
                answer, max_sum = level, s
            q = nq
        return answer
