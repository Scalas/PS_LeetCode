from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def reverse_odd_levels(root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node1, node2, d):
            n1, p1 = node1
            n2, p2 = node2
            if d == 0:
                p1.left, p2.right = n2, n1
            else:
                p1.right, p2.left = n2, n1
            if n1.left:
                n1.left, n1.right, n2.left, n2.right = (
                    n2.left,
                    n2.right,
                    n1.left,
                    n1.right,
                )

        q = [[root, None]]
        level = 0
        while q:
            nq = []
            for cur, _ in q:
                if cur.left:
                    nq.append([cur.left, cur])
                if cur.right:
                    nq.append([cur.right, cur])
            if level % 2:
                for i in range(len(q) // 2):
                    swap(q[i], q[len(q) - i - 1], i % 2)
            level += 1
            q = nq
        return root
