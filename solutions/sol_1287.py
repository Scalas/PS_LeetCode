from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def find_special_integer(arr: List[int]) -> int:
        q = len(arr) // 4 + 1
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
            if count[num] == q:
                return num
