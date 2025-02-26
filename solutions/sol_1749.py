from typing import List


class Solution:
    @staticmethod
    def max_absolute_sum(nums: List[int]) -> int:
        n = len(nums)
        ma = mi = nums[0]
        answer = max(ma, -mi)
        for i in range(1, n):
            num = nums[i]
            ma = max(num, num + ma)
            mi = min(num, num + mi)
            answer = max(answer, ma, -mi)
        return answer
