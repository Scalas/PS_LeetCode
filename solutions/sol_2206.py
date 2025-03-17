from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def divide_array(nums: List[int]) -> bool:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        return sum([c % 2 for c in cnt.values()]) == 0
