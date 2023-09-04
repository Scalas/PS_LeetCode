from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def has_cycle(head: Optional[ListNode]) -> bool:
        visited = 10**6
        while head:
            if head.val == visited:
                return True
            head.val = visited
            head = head.next
        return False
