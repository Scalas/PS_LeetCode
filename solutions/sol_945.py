from typing import List


class Solution:
    @staticmethod
    def min_increment_for_unique(nums: List[int]) -> int:
        nums.sort()
        last = -1
        answer = 0
        for num in nums:
            if num <= last:
                answer += last - num + 1
                last += 1
            else:
                last = num
        return answer
