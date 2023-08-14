from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def add_two_numbers(
        l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1, num2 = [], []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        res = int("".join(map(str, num1))) + int("".join(map(str, num2)))

        if res == 0:
            return ListNode(0)

        answer = None
        while res > 0:
            node = ListNode(res % 10)
            node.next = answer
            answer = node
            res //= 10
        return answer
