from typing import List


class Solution:
    @staticmethod
    def min_swaps(nums: List[int]) -> int:
        n = len(nums)
        m = nums[0]
        nums *= 2
        for i in range(1, n * 2):
            if i < n:
                m += nums[i]
            nums[i] += nums[i - 1]
        nums.append(0)

        answer = m
        for i in range(n):
            j = i + m - 1
            answer = min(answer, m - nums[j] + nums[i - 1])

        return answer
