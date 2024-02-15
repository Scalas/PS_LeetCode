from typing import List


class Solution:
    @staticmethod
    def largest_perimeter(nums: List[int]) -> int:
        nums.sort()
        answer = -1
        s = nums[0] + nums[1]
        for num in nums[2:]:
            if s > num:
                answer = s + num
            s += num
        return answer
