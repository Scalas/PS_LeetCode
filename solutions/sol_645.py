from typing import List


class Solution:
    @staticmethod
    def find_error_nums(nums: List[int]) -> List[int]:
        missing = list(set(range(1, len(nums) + 1)) - set(nums))[0]
        s = set()
        for num in nums:
            if num in s:
                return [num, missing]
            s.add(num)
