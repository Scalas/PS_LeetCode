from typing import List


class Solution:
    @staticmethod
    def array_rank_transform(arr: List[int]) -> List[int]:
        rank = dict()
        idx = 0
        for num in sorted(set(arr)):
            idx += 1
            rank[num] = idx
        return list(map(lambda x: rank[x], arr))
