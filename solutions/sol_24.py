from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if head and head.next:
            head = head.next
        pre = None
        while cur and cur.next:
            nxt = cur.next
            if pre:
                pre.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            pre = cur
            cur = cur.next
        return head
