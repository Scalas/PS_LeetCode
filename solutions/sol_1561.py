from typing import List


class Solution:
    @staticmethod
    def max_coins(piles: List[int]) -> int:
        piles.sort()
        return sum(piles[len(piles) // 3 :: 2])
