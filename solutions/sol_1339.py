from typing import Optional
from leet_code_types.leet_code_types import TreeNode


class Solution:

    mod = 10 ** 9 + 7

    @staticmethod
    def max_product(root: Optional[TreeNode]) -> int:

        nodes = []

        def dfs(cur):
            res = cur.val
            if cur.left:
                res += dfs(cur.left)
            if cur.right:
                res += dfs(cur.right)
            cur.val = res
            nodes.append(cur)
            return res

        dfs(root)

        answer = 0
        total = root.val

        for node in nodes:
            answer = max(answer, node.val * (total - node.val))

        return answer % Solution.mod
