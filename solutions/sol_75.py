from typing import List


class Solution:
    @staticmethod
    def sort_colors(nums: List[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1
        idx = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[idx] = i
                idx += 1
