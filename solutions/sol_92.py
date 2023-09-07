from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def reverse_between(
        head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        cur = head
        begin = None
        for i in range(left - 1):
            if i == left - 2:
                begin = cur
            cur = cur.next

        end = cur
        pre = end
        cur = cur.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        end.next = cur
        if begin:
            begin.next = pre
            return head
        else:
            return pre
