from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def successful_pairs(
        spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        answer = []
        for spell in spells:
            min_p = success / spell
            answer.append(n - bisect_left(potions, min_p))
        return answer
