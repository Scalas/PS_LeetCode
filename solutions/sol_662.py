from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def width_of_binary_tree(root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        answer = 1

        while q:
            nq = []
            for cur, idx in q:
                if cur.left:
                    nq.append((cur.left, idx * 2))
                if cur.right:
                    nq.append((cur.right, idx * 2 + 1))
            if len(nq) > 1:
                answer = max(answer, nq[-1][1] - nq[0][1] + 1)
            q = nq
        return answer
