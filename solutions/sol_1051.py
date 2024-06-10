from typing import List


class Solution:
    @staticmethod
    def height_checker(heights: List[int]) -> int:
        s = sorted(heights)
        return sum([1 if heights[i] != s[i] else 0 for i in range(len(heights))])
