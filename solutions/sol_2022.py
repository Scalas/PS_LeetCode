from typing import List


class Solution:
    @staticmethod
    def construct_2d_array(original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []
        res = [[0] * n for _ in range(m)]
        idx = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = original[idx]
                idx += 1
        return res
