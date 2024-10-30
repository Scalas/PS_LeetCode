from typing import List


class Solution:
    @staticmethod
    def minimum_mountain_removals(nums: List[int]) -> int:
        n = len(nums)
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            res = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, left[j] + 1)
            left[i] = res
        for i in range(n - 1, -1, -1):
            res = 0
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    res = max(res, right[j] + 1)
            right[i] = res

        return n - max(
            [left[i] + right[i] + 1 for i in range(n) if left[i] > 0 and right[i] > 0]
        )
