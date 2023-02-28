from collections import defaultdict
from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def find_duplicate_subtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        group = defaultdict(list)

        def dfs(cur):
            key = f'{cur.val}'
            if cur.left:
                key = dfs(cur.left) + 'L' + key
            if cur.right:
                key = key + 'R' + dfs(cur.right)
            group[key].append(cur)
            return key
        dfs(root)

        answer = []
        for nodes in group.values():
            if len(nodes) > 1:
                answer.append(nodes[0])
        return answer
