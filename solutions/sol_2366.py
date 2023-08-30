from typing import List
from math import ceil


class Solution:
    @staticmethod
    def minimum_replacement(nums: List[int]) -> int:
        answer = 0
        pre = 10 ** 9 + 1

        while nums:
            num = nums.pop()
            if num <= pre:
                pre = num
                continue
            slot = ceil(num / pre)
            last = num // slot
            answer += slot - 1
            pre = last
        return answer
