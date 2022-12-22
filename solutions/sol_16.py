from bisect import bisect_right
from typing import List


class Solution:
    @staticmethod
    def three_sum_closest(nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        two_sum = dict()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                s = nums[i] + nums[j]
                if s not in two_sum:
                    two_sum[s] = j + 1

        answer = sum(nums[0:3])
        for ts, start in two_sum.items():
            idx = bisect_right(nums, target - ts, start, n)

            if idx < n:
                three_sum = ts + nums[idx]
                if abs(three_sum - target) < abs(answer - target):
                    answer = three_sum
            if idx - 1 >= start:
                three_sum = ts + nums[idx - 1]
                if abs(three_sum - target) < abs(answer - target):
                    answer = three_sum
        return answer
