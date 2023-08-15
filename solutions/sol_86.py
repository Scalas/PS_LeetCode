from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        p1, p2, c1, c2 = None, None, None, None

        cur = head
        while cur:
            if cur.val < x:
                if c1:
                    c1.next = cur
                    c1 = cur
                else:
                    p1 = c1 = cur
            else:
                if c2:
                    c2.next = cur
                    c2 = cur
                else:
                    p2 = c2 = cur
            cur = cur.next
        if c1:
            c1.next = p2
        if c2:
            c2.next = None
        return p1 if p1 else p2
