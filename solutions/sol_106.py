from typing import List, Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def build_tree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = dict()
        n = len(inorder)
        for i in range(n):
            inorder_index[inorder[i]] = i

        def dfs(pl, pr, il, ir):
            mid = postorder[pr]
            cur = TreeNode(mid)
            mid_idx = inorder_index[mid]
            if mid_idx > il:
                cur.left = dfs(pl, pl + mid_idx - il - 1, il, mid_idx - 1)
            if mid_idx < ir:
                cur.right = dfs(pl + mid_idx - il, pr - 1, mid_idx + 1, ir)
            return cur

        return dfs(0, n - 1, 0, n - 1)
