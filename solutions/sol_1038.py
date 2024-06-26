from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def bst_to_gst(root: TreeNode) -> TreeNode:
        acc = 0

        def dfs(cur: TreeNode):
            nonlocal acc
            if cur.right:
                dfs(cur.right)
            res = cur.val + acc
            acc += cur.val
            cur.val = res
            if cur.left:
                dfs(cur.left)

        dfs(root)
        return root
