from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while head:
            nxt = head.next
            head.next = res
            res = head
            head = nxt
        return res
