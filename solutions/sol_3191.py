from typing import List


class Solution:
    @staticmethod
    def min_operations(nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n - 2):
            if nums[i] == 1:
                continue
            for j in range(3):
                nums[i + j] = 1 - nums[i + j]
            answer += 1
        if sum(nums[-3:]) < 3:
            return -1
        return answer
