from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def is_palindrome(head: Optional[ListNode]) -> bool:
        n = 0
        cursor = head
        while cursor:
            n += 1
            cursor = cursor.next
        cursor1, cursor2 = None, head
        for _ in range(n // 2):
            nxt = cursor2.next
            cursor2.next = cursor1
            cursor1 = cursor2
            cursor2 = nxt
        if n % 2:
            cursor2 = cursor2.next
        while cursor1 and cursor2:
            if cursor1.val != cursor2.val:
                return False
            cursor1, cursor2 = cursor1.next, cursor2.next
        return True
