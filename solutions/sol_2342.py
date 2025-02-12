from collections import defaultdict
from heapq import heapify, heappop
from typing import List


class Solution:
    @staticmethod
    def maximum_sum(nums: List[int]) -> int:
        digit_sum = defaultdict(list)
        for num in nums:
            v = num
            ds = 0
            while v:
                ds += v % 10
                v //= 10
            digit_sum[ds].append(-num)
        answer = -1
        for group in digit_sum.values():
            if len(group) < 2:
                continue
            heapify(group)
            answer = max(answer, -heappop(group) - heappop(group))
        return answer
