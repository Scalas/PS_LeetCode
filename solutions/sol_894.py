from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def all_possible_fbt(n: int) -> List[Optional[TreeNode]]:
        def copy(r: Optional[TreeNode]):
            res = TreeNode(0)
            if r.left:
                res.left = copy(r.left)
            if r.right:
                res.right = copy(r.right)
            return res

        def get_leaves(r: TreeNode):
            leaves = []
            q = [r]
            while q:
                nq = []
                for cur in q:
                    if cur.left == cur.right is None:
                        leaves.append(cur)
                    else:
                        if cur.left:
                            nq.append(cur.left)
                        if cur.right:
                            nq.append(cur.right)
                q = nq
            return leaves

        def tree_to_key(r: TreeNode):
            res = []
            q = [r]
            while q:
                nq = []
                for cur in q:
                    if not cur:
                        res.append("-")
                    else:
                        res.append("0")
                        nq.append(cur.left)
                        nq.append(cur.right)
                q = nq
            return "".join(res)

        if n % 2 == 0:
            return []

        root = TreeNode(0)
        q = [root]
        for _ in range(n // 2):
            nq = dict()
            for cur in q:
                leaves = get_leaves(cur)
                for leaf in leaves:
                    leaf.left = TreeNode(0)
                    leaf.right = TreeNode(0)
                    nt = copy(cur)
                    nq[tree_to_key(nt)] = nt
                    leaf.left = leaf.right = None
            q = nq.values()
        return list(q)
