from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def double_it(head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res = ListNode(0)
        tail = res
        last = 0
        while cur:
            val = cur.val * 2
            tail.next = ListNode(last + val // 10)
            last = val % 10
            tail = tail.next
            cur = cur.next
        tail.next = ListNode(last)
        while res.val == 0 and res.next:
            res = res.next
        return res
