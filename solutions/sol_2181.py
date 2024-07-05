from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def merge_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        tail = h
        v = 0
        cur = head
        while cur:
            if cur.val != 0:
                v += cur.val
            elif v > 0:
                tail.next = ListNode(v)
                v = 0
                tail = tail.next
            cur = cur.next
        return h.next
