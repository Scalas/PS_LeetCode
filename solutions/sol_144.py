from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
        path = []

        def dfs(cur):
            if cur is None:
                return
            path.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)

        dfs(root)
        return path
