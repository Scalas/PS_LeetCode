from typing import List


class Solution:
    @staticmethod
    def find_duplicate(nums: List[int]) -> int:
        count = [0] * (10**5 + 1)
        for num in nums:
            if count[num] == 1:
                return num
            count[num] += 1
