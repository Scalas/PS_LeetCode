from typing import List


class Solution:
    @staticmethod
    def min_operations(nums: List[int]) -> int:
        t = len(nums)
        s, e = 0, 0
        nums = sorted(set(nums))
        n = len(nums)
        max_length = 0
        while e < n:
            while nums[e] - nums[s] >= t:
                s += 1
            max_length = max(max_length, e - s + 1)
            e += 1
        return t - max_length
