from typing import List


class Solution:
    @staticmethod
    def max_ascending_sum(nums: List[int]) -> int:
        answer, acc, last = 0, 0, 0
        for num in nums:
            if num > last:
                acc += num
            else:
                answer = max(answer, acc)
                acc = num
            last = num

        return max(answer, acc)


