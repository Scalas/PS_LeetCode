from random import randint
from typing import Optional

from leet_code_types.leet_code_types import ListNode


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        self.size = len(self.nums)

    def get_random(self) -> int:
        return self.nums[randint(0, self.size - 1)]
