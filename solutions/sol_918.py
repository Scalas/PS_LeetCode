from typing import List


class Solution:
    @staticmethod
    def max_sub_array_sum_circular(nums: List[int]) -> int:
        n = len(nums)
        acc = nums[:]
        for i in range(1, n):
            acc[i] += acc[i - 1]
        rev_acc = nums[:] + [0]
        for i in range(n - 2, -1, -1):
            rev_acc[i] += rev_acc[i + 1]
        for i in range(n - 2, -1, -1):
            rev_acc[i] = max(rev_acc[i], rev_acc[i + 1])
        dp = nums[:]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        answer = max(dp)
        for i in range(n):
            answer = max(answer, acc[i] + rev_acc[i + 1])
        return answer
