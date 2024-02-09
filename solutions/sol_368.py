from typing import List


class Solution:
    @staticmethod
    def largest_divisible_subset(nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [-1, 1]
        end, mc = 0, 1
        for i in range(1, n):
            num1 = nums[i]
            pre, cnt = -1, 1
            for j in range(i):
                num2 = nums[j]
                if num1 % num2 == 0:
                    tcnt = dp[j][1] + 1
                    if tcnt > cnt:
                        pre, cnt = j, tcnt
            if cnt > mc:
                end, mc = i, cnt
            dp[i] = [pre, cnt]

        answer = []
        while end != -1:
            answer.append(nums[end])
            end = dp[end][0]
        return answer[::-1]
