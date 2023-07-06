from typing import List


class Solution:
    @staticmethod
    def min_sub_array_len(target: int, nums: List[int]) -> int:
        s, e = 0, 0
        total = 0
        INF = len(nums) + 1
        answer = INF
        for i in range(len(nums)):
            total += nums[i]
            i += 1
            while total >= target:
                answer = min(answer, i - s)
                total -= nums[s]
                s += 1
        return answer if answer != INF else 0
