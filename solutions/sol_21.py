from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return head.next
