from typing import List


class Solution:
    @staticmethod
    def divide_array(nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arrays = [
            [nums[3 * i], nums[3 * i + 1], nums[3 * i + 2]] for i in range(n // 3)
        ]
        max_diff = max(map(lambda x: max(x) - min(x), arrays))
        return arrays if max_diff <= k else []
