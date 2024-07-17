from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def del_nodes(root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []

        def dfs(cur, parent, is_left):
            left, right = cur.left, cur.right
            cur.left = cur.right = None
            if cur.val not in to_delete:
                if parent:
                    if is_left:
                        parent.left = cur
                    else:
                        parent.right = cur
                else:
                    res.append(cur)
                if left:
                    dfs(left, cur, True)
                if right:
                    dfs(right, cur, False)
            else:
                if left:
                    dfs(left, None, False)
                if right:
                    dfs(right, None, False)

        dfs(root, None, False)
        return res
