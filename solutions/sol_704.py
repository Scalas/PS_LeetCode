from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        if idx == len(nums) or nums[idx] != target:
            return -1
        return idx
