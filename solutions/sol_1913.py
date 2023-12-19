from typing import List


class Solution:
    @staticmethod
    def max_product_difference(nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
