from typing import List


class Solution:
    @staticmethod
    def get_sum_absolute_differences(nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            nums[i + 1] += nums[i]
        nums.append(0)
        answer = []
        for i in range(n):
            num = nums[i] - nums[i - 1]
            answer.append(
                num * (i + 1) - nums[i] + nums[n - 1] - nums[i - 1] - num * (n - i)
            )
        return answer
