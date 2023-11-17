from typing import List


class Solution:
    @staticmethod
    def min_pair_sum(nums: List[int]) -> int:
        nums.sort()
        answer = 0
        n = len(nums)
        for i in range(n // 2):
            answer = max(answer, nums[i] + nums[n - 1 - i])
        return answer
