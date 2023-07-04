from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def single_number(nums: List[int]) -> int:
        return [num for num, cnt in Counter(nums).items() if cnt == 1][0]
