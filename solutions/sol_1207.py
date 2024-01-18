from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def unique_occurrences(arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        occur = set()
        for cnt in count.values():
            if cnt in occur:
                return False
            occur.add(cnt)
        return True
