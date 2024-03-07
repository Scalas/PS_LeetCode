from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        return arr[len(arr) // 2]
