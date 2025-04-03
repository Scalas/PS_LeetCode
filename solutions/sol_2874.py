from typing import List


class Solution:
    @staticmethod
    def maximum_triplet_value(nums: List[int]) -> int:
        n = len(nums)
        rm = [-1] * n
        rm[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rm[i] = max(nums[i], rm[i + 1])
        answer = 0
        pm = nums[0]
        for i in range(1, n - 1):
            answer = max(answer, (pm - nums[i]) * rm[i + 1])
            pm = max(pm, nums[i])
        return answer
