from typing import List


class Solution:
    @staticmethod
    def sort_people(names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(range(len(heights)), key=lambda x: -heights[x])]
