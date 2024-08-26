from typing import List

from leet_code_types.leet_code_types import NaryTreeNode


class Solution:
    @staticmethod
    def postorder(root: NaryTreeNode) -> List[int]:
        answer = []

        def dfs(cur):
            nonlocal answer

            for child in cur.children:
                dfs(child)
            answer.append(cur.val)

        if not root:
            return answer

        dfs(root)
        return answer
