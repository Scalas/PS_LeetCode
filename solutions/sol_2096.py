from collections import defaultdict
from typing import Optional

from leet_code_types.leet_code_types import TreeNode


class Solution:
    @staticmethod
    def get_directions(
        root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        start = None
        parent = dict()
        parent[root.val] = None

        def traverse(node):
            nonlocal start
            if node.val == startValue:
                start = node
            if node.left:
                parent[node.left.val] = node
                traverse(node.left)
            if node.right:
                parent[node.right.val] = node
                traverse(node.right)

        traverse(root)

        q = [start]
        command = dict()
        visited = defaultdict(bool)
        command[start.val] = ""
        visited[start.val] = True
        while q:
            nq = []
            for node in q:
                if parent[node.val]:
                    next_value = parent[node.val].val
                    if not visited[next_value]:
                        visited[next_value] = True
                        command[next_value] = (node.val, "U")
                        nq.append(parent[node.val])
                if node.left:
                    next_value = node.left.val
                    if not visited[next_value]:
                        visited[next_value] = True
                        command[next_value] = (node.val, "L")
                        nq.append(node.left)
                if node.right:
                    next_value = node.right.val
                    if not visited[next_value]:
                        visited[next_value] = True
                        command[next_value] = (node.val, "R")
                        nq.append(node.right)
            q = nq

        answer = []
        dest = destValue
        while dest != startValue:
            p, c = command[dest]
            answer.append(c)
            dest = p
        return "".join(answer[::-1])
