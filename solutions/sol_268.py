from typing import List


class Solution:
    @staticmethod
    def missing_number(nums: List[int]) -> int:
        s = set(range(len(nums) + 1))
        print(s)
        for num in nums:
            if num in s:
                s.remove(num)
        return list(s)[0]
