from typing import List


class Solution:
    @staticmethod
    def ways_to_split_array(nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        answer = 0
        for i in range(n - 1):
            left = nums[i]
            right = nums[-1] - nums[i]
            if left >= right:
                answer += 1
        return answer
