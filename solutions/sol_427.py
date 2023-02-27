from typing import List
from leet_code_types.leet_code_types import QuadTreeNode


class Solution:
    @staticmethod
    def construct(grid: List[List[int]]) -> QuadTreeNode:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i < n - 1:
                    grid[i + 1][j] += grid[i][j]
                if j > 0:
                    grid[i][j] += grid[i][j - 1]

        def link_to_parent(parent_node, child_position, child_node):
            if not parent_node:
                return
            if child_position == 0:
                parent_node.top_left = child_node
            elif child_position == 1:
                parent_node.top_right = child_node
            elif child_position == 2:
                parent_node.bottom_left = child_node
            else:
                parent_node.bottom_right = child_node

        def dfs(parent, position, tr, tc, br, bc):
            acc = grid[br][bc]
            if tc > 0:
                acc -= grid[br][tc - 1]
            if tr > 0:
                acc -= grid[tr - 1][bc]
            if tc > 0 and tr > 0:
                acc += grid[tr - 1][tc - 1]
            full_size = (br - tr + 1) * (bc - tc + 1)
            if acc == full_size:
                node = QuadTreeNode(1, 1, None, None, None, None)
                link_to_parent(parent, position, node)
                return
            if acc == 0:
                node = QuadTreeNode(0, 1, None, None, None, None)
                link_to_parent(parent, position, node)
                return
            node = QuadTreeNode(1, 0, None, None, None, None)
            link_to_parent(parent, position, node)

            half = (br - tr + 1) // 2
            dfs(node, 0, tr, tc, tr + half - 1, tc + half - 1)
            dfs(node, 1, tr, tc + half, br - half, bc)
            dfs(node, 2, tr + half, tc, br, bc - half)
            dfs(node, 3, tr + half, tc + half, br, bc)
            return node

        ta = grid[-1][-1]
        if ta == 0:
            return QuadTreeNode(0, 1, None, None, None, None)
        if grid[-1][-1] == n * n:
            return QuadTreeNode(1, 1, None, None, None, None)

        root = dfs(None, 0, 0, 0, n - 1, n - 1)

        return root
