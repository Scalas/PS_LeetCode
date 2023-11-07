from math import ceil
from typing import List


class Solution:
    @staticmethod
    def eliminate_maximum(dist: List[int], speed: List[int]) -> int:
        w = [ceil(dist[i] / speed[i]) for i in range(len(dist))]
        w.sort()
        for i in range(len(dist)):
            if w[i] < i + 1:
                return i
        return len(dist)
