from typing import Optional

from leet_code_types.leet_code_types import ListNodeWithRandomPointer


class Solution:
    @staticmethod
    def copy_random_list(head: 'Optional[ListNodeWithRandomPointer]') -> 'Optional[ListNodeWithRandomPointer]':
        nodes = []
        while head:
            head.id = len(nodes)
            nodes.append(ListNodeWithRandomPointer(head.val, head.next, head.random))
            head = head.next

        for node in nodes:
            if node.next:
                node.next = nodes[node.next.id]
            if node.random:
                node.random = nodes[node.random.id]
        return nodes[0] if nodes else None
