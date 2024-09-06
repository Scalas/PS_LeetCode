from typing import List, Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def modified_list(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        tail = h
        nums = set(nums)
        cur = head
        while cur:
            if cur.val in nums:
                cur = cur.next
            else:
                tail.next = cur
                tail = tail.next
                cur = cur.next
                tail.next = None
        return h.next
