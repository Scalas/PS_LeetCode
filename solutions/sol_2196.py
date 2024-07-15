from collections import defaultdict
from typing import List, Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def create_binary_tree(descriptions: List[List[int]]) -> Optional[TreeNode]:
        g = defaultdict(TreeNode)
        degree = defaultdict(int)
        for u, v, is_left in descriptions:
            if u not in g:
                g[u] = TreeNode(u)
            if v not in g:
                g[v] = TreeNode(v)
            if is_left:
                g[u].left = g[v]
            else:
                g[u].right = g[v]
            degree[v] += 1

        for node in g:
            if degree[node] == 0:
                return g[node]
