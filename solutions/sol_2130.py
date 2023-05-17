from typing import Optional
from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def pair_sum(head: Optional[ListNode]) -> int:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        m = n // 2
        answer = 0
        nums = []
        cur = head
        for _ in range(m):
            nums.append(cur.val)
            cur = cur.next
        for _ in range(m):
            answer = max(answer, nums.pop() + cur.val)
            cur = cur.next
        return answer
