from typing import List


class Solution:
    @staticmethod
    def combination_sum4(nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * 1001

        def dfs(csum):
            if csum == target:
                return 1
            if csum > target:
                return 0
            if dp[csum] == -1:
                res = 0
                for num in nums:
                    res += dfs(csum + num)
                dp[csum] = res
            return dp[csum]

        return dfs(0)
