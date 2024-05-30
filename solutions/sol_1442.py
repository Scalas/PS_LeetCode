from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def count_triplets(arr: List[int]) -> int:
        def xor(o1, o2):
            return (~o1 & o2) | (o1 & ~o2)

        def range_xor(i1, i2):
            res = arr[i2]
            if i1 > 0:
                res = xor(res, arr[i1 - 1])
            return res

        n = len(arr)
        for i in range(1, n):
            arr[i] = xor(arr[i - 1], arr[i])

        count = [defaultdict(int) for _ in range(n)]
        for i in range(1, n):
            for j in range(i, n):
                count[i][range_xor(i, j)] += 1

        answer = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = range_xor(i, j - 1)
                answer += count[j][x]
        return answer
