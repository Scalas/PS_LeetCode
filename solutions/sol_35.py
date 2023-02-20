from typing import List
from bisect import bisect_left


class Solution:
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
