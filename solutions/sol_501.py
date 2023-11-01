from collections import defaultdict
from typing import Optional, List

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def find_mode(root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)

        def dfs(cur):
            count[cur.val] += 1
            if cur.left:
                dfs(cur.left)
            if cur.right:
                dfs(cur.right)

        dfs(root)

        max_count = max(count.values())

        return [i for i, cnt in count.items() if cnt == max_count]
