from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def can_be_equal(target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in target:
            count[num] += 1
        for num in arr:
            if count[num] <= 0:
                return False
            count[num] -= 1
        return True
