from typing import List


class Solution:
    @staticmethod
    def maximum_happiness_sum(happiness: List[int], k: int) -> int:
        res = 0
        happiness.sort()
        for i in range(k):
            res += max(happiness.pop() - i, 0)
        return res
