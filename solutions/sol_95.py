from typing import List, Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def generate_trees(n: int) -> List[Optional[TreeNode]]:
        arr = range(1, n + 1)

        def dfs(s, e):
            if s > e:
                return [None]

            res = []
            for idx in range(s, e + 1):
                val = arr[idx]
                left = dfs(s, idx - 1)
                right = dfs(idx + 1, e)
                for l in left:
                    for r in right:
                        root = TreeNode(val)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return dfs(0, n - 1)
