from typing import List


class Solution:
    @staticmethod
    def rearrange_array(nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        pi, ni = 0, 1
        h = len(nums) // 2
        for num in nums:
            if num > 0:
                answer[pi] = num
                pi += 2
            else:
                answer[ni] = num
                ni += 2
        return answer
