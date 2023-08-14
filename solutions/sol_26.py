from typing import List


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        answer = []
        for num in nums:
            if answer and answer[-1] == num:
                continue
            answer.append(num)
        nums[: len(answer)] = answer
        return len(answer)
