from math import floor
from typing import List


class Solution:
    @staticmethod
    def get_averages(nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = k * 2 + 1
        answer = [-1] * n
        if n < m:
            return answer
        s = sum(nums[:k * 2 + 1])
        answer[k] = floor(s / m)
        for i in range(k + 1, n - k):
            s += (nums[i + k] - nums[i - k - 1])
            answer[i] = floor(s / m)
        return answer
