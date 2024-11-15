from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    @staticmethod
    def count_fair_pairs(nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        answer = 0
        for i in range(n):
            num = nums[i]
            li = max(bisect_left(nums, lower - num), i + 1)
            ri = bisect_right(nums, upper - num)
            answer += max(ri - li, 0)
        return answer
