from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def remove_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nxt = cur.next
            while nodes and nodes[-1].val < cur.val:
                nodes.pop()
            nodes.append(cur)
            cur = nxt
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
