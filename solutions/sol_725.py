from typing import Optional, List

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def split_list_to_parts(
        head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        slots = [length // k] * k
        for i in range(length % k):
            slots[i] += 1

        res = []
        cur = head
        for slot in slots:
            if not slot:
                res.append(None)
                continue
            res.append(cur)
            for _ in range(slot - 1):
                cur = cur.next
            nxt_cur = cur.next
            cur.next = None
            cur = nxt_cur
        return res
