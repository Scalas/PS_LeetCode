from typing import List


class Solution:
    @staticmethod
    def three_consecutive_odds(arr: List[int]) -> bool:
        odd = 0
        for num in arr:
            if num % 2:
                odd += 1
            else:
                odd = 0
            if odd == 3:
                return True
        return False
