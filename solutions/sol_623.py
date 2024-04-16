from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def add_one_row(
        root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        q = [root]
        d = 1
        while q and d < depth - 1:
            nq = []
            for cur in q:
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            q = nq
            d += 1
        for node in q:
            original_left = node.left
            original_right = node.right
            left = TreeNode(val, original_left, None)
            right = TreeNode(val, None, original_right)
            node.left = left
            node.right = right
        return root
