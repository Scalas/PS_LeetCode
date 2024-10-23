from collections import defaultdict
from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def replace_value_in_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [[0, 0, root]]
        while q:
            nq = []
            total = 0
            psum = defaultdict(int)
            idx = 0
            for parent, cur_id, cur in q:
                total += cur.val
                psum[parent] += cur.val
                if cur.left:
                    nq.append([cur_id, idx, cur.left])
                    idx += 1
                if cur.right:
                    nq.append([cur_id, idx, cur.right])
                    idx += 1
            for parent, cur_id, cur in q:
                cur.val = total - psum[parent]
            q = nq
        return root
