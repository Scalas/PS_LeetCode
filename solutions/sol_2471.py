from collections import defaultdict
from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def minimum_operations(root: Optional[TreeNode]) -> int:
        q = [root]
        answer = 0
        while q:
            index = defaultdict(int)
            for i in range(len(q)):
                index[q[i].val] = i
            sq = sorted([q[i].val for i in range(len(q))])
            for i in range(len(q)):
                num = q[i].val
                tnum = sq[i]
                ti = index[sq[i]]
                if num != tnum:
                    answer += 1
                    q[i].val, q[ti].val = q[ti].val, q[i].val
                    index[num] = ti
                    index[tnum] = i
            nq = []
            for cur in q:
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            q = nq
        return answer
