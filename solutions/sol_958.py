from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def is_complete_tree(root: Optional[TreeNode]) -> bool:
        tree = [-1]
        q = [(root, 1)]
        while q:
            nq = []
            for cur, idx in q:
                if len(tree) < idx:
                    return False
                tree.append(cur.val)
                if cur.left:
                    nq.append((cur.left, idx * 2))
                if cur.right:
                    nq.append((cur.right, idx * 2 + 1))
            q = nq

        return True
