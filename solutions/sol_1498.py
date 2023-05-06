from typing import List
from bisect import bisect_right


class Solution:
    @staticmethod
    def num_subseq(nums: List[int], target: int) -> int:
        nums.sort()
        bound = dict()

        def get_max_bound(n):
            if n not in bound:
                bound[n] = bisect_right(nums, n)
            return bound[n]

        answer = 0
        mod = 10 ** 9 + 7
        for i in range(len(nums)):
            num = nums[i]
            b = get_max_bound(target - num)
            if b - i <= 0:
                continue
            answer = (answer + 2 ** (b - i - 1)) % mod
        return answer
