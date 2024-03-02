from typing import List


class Solution:
    @staticmethod
    def sorted_squares(nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])
