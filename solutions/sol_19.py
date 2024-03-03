from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pos = head
        cache = []
        sz = 0
        while pos:
            cache.append(pos)
            sz += 1
            pos = pos.next

        target = cache[sz - n]
        pre, nxt = None, None
        if n < sz:
            pre = cache[sz - n - 1]
        if n > 1:
            nxt = cache[sz - n + 1]

        if pre:
            pre.next = nxt
            return cache[0]
        else:
            return nxt
