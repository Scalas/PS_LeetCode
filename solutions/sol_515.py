from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def largest_values(root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        INF = 10**10
        q = [root]
        answer = []
        while q:
            nq = []
            mv = -INF
            for cur in q:
                mv = max(mv, cur.val)
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            answer.append(mv)
            q = nq
        return answer
