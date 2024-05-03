from typing import List


class Solution:
    @staticmethod
    def find_max_k(nums: List[int]) -> int:
        ngs = set(nums)
        nums.sort(reverse=True)
        for num in nums:
            if -num in ngs:
                return num
        return -1
