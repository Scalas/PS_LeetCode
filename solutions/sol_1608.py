from typing import List
from bisect import bisect_left


class Solution:
    @staticmethod
    def special_array(nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1, n + 1):
            count = n - bisect_left(nums, i)
            if i == count:
                return i
        return -1
