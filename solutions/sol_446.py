from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def number_of_arithmetic_slices(nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = [[defaultdict(int) for _ in range(2)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][0][diff] += 1
        answer = 0
        for i in range(2, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                res = dp[j][0][diff] + dp[j][1][diff]
                answer += res
                dp[i][1][diff] += res
        return answer
