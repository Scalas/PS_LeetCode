from typing import List


class Solution:
    @staticmethod
    def zero_filled_sub_array(nums: List[int]) -> int:
        answer = 0
        count = 0
        for num in nums:
            if num:
                answer += (count * (count + 1) // 2)
                count = 0
            else:
                count += 1
        answer += (count * (count + 1) // 2)
        return answer
