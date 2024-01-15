from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_winners(matches: List[List[int]]) -> List[List[int]]:
        lc = defaultdict(int)
        for u, v in matches:
            lc[v] += 1
            lc[u]
        lc = lc.items()

        return [
            sorted([u for u, v in lc if v == 0]),
            sorted([u for u, v in lc if v == 1]),
        ]
