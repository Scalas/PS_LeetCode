from typing import List


class Solution:
    @staticmethod
    def longest_monotonic_subarray(nums: List[int]) -> int:
        n = len(nums)
        s, e = 0, 1
        answer = 0
        while s < n:
            while e < n and nums[e] > nums[e - 1]:
                e += 1
            answer = max(answer, e - s)
            s, e = e, e + 1
        s, e = 0, 1
        while s < n:
            while e < n and nums[e] < nums[e - 1]:
                e += 1
            answer = max(answer, e - s)
            s, e = e, e + 1
        return answer
