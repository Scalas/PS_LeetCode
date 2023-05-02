from typing import List


class Solution:
    @staticmethod
    def array_sign(nums: List[int]) -> int:
        answer = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                answer *= -1
        return answer
