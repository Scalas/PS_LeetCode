from typing import List


class Solution:
    @staticmethod
    def valid_partition(nums: List[int]) -> bool:
        n = len(nums)
        if n == 2:
            return nums[0] == nums[1]

        dp = [False] * n
        dp[1] = nums[0] == nums[1]
        dp[2] = nums[0] == nums[1] == nums[2] or nums[2] - nums[1] == nums[1] - nums[0] == 1

        for i in range(3, n):
            if dp[i - 2] and nums[i - 1] == nums[i]:
                dp[i] = True
                continue
            if dp[i - 3]:
                if nums[i - 2] == nums[i - 1] == nums[i]:
                    dp[i] = True
                    continue
                if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] == 1:
                    dp[i] = True
        return dp[n - 1]
