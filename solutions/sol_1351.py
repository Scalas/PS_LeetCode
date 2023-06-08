from typing import List


class Solution:
    @staticmethod
    def count_negatives(grid: List[List[int]]) -> int:
        return sum([len([num for num in line if num < 0]) for line in grid])
