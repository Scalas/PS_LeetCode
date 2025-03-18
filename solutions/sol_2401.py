from typing import List


class Solution:
    @staticmethod
    def longest_nice_subarray(nums: List[int]) -> int:
        n = len(nums)
        answer = 1
        bit = nums[0]
        left = 0
        for i in range(1, n):
            num = nums[i]
            while bit & num != 0:
                bit -= nums[left]
                left += 1
            bit += num
            answer = max(answer, i - left + 1)
        return answer
