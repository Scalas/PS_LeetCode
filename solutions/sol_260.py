from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def single_number(nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[str(num)] += 1
        return [int(key) for key in count.keys() if count[key] == 1]
