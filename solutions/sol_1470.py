from typing import List


class Solution:
    @staticmethod
    def shuffle(nums: List[int], n: int) -> List[int]:
        return [nums[i + j * n] for i in range(n) for j in range(2)]
