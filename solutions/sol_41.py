from typing import List


class Solution:
    @staticmethod
    def first_missing_positive(nums: List[int]) -> int:
        s = set()
        while nums:
            s.add(nums.pop())
        i = 1
        while i in s:
            i += 1
        return i
