from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def swap_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        n = len(nodes)
        u, v = k - 1, n - k
        if u != v:
            nodes[u], nodes[v] = nodes[v], nodes[u]
            if u > 0:
                nodes[u - 1].next = nodes[u]
            if u < n - 1:
                nodes[u].next = nodes[u + 1]
            else:
                nodes[u].next = None

            if v > 0:
                nodes[v - 1].next = nodes[v]
            if v < n - 1:
                nodes[v].next = nodes[v + 1]
            else:
                nodes[v].next = None
        return nodes[0]
