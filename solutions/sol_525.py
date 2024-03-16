from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_max_length(nums: List[int]) -> int:
        nums = list(map(lambda x: x if x == 1 else -1, nums))
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        answer = d[0][-1] + 1 if d[0] else 0
        for r in d.values():
            if len(r) < 2:
                continue
            answer = max(answer, r[-1] - r[0])
        return answer
