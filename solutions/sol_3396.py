from math import ceil
from typing import List


class Solution:
    @staticmethod
    def minimum_operations(nums: List[int]) -> int:
        s = set()
        n = len(nums)
        target = 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num not in s:
                s.add(num)
            else:
                target = i + 1
                break
        return ceil(target / 3)
