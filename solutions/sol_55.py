from typing import List


class Solution:
    @staticmethod
    def can_jump(nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [0] * (n + 1)
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1]
            max_dist = min(n - 1, i + nums[i])
            if dp[i + 1] - dp[max_dist + 1]:
                dp[i] += 1
        return dp[0] - dp[1] == 1
