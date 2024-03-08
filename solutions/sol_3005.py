from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def max_frequency_elements(nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        m = max(count.values())
        return sum([c for c in count.values() if c == m])
