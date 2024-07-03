from typing import List


class Solution:
    @staticmethod
    def min_difference(nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n < 5:
            return 0
        k = n - 3
        answer = nums[k - 1] - nums[0]
        for i in range(1, n - k + 1):
            answer = min(answer, nums[i + k - 1] - nums[i])
        return answer
