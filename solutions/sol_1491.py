from typing import List


class Solution:
    @staticmethod
    def average(salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)
