from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def reorder_list(head: Optional[ListNode]) -> None:
        cursor = head
        nodes = []
        while cursor:
            nodes.append(cursor)
            cursor = cursor.next

        n = len(nodes)
        for i in range(n - n // 2):
            node = nodes[i]
            nxt = node.next
            if i == n - n // 2 - 1:
                nxt = None
            insert = nodes[n - 1 - i]
            node.next = insert
            insert.next = nxt
