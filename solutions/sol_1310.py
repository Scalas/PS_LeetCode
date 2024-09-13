from typing import List


class Solution:
    @staticmethod
    def xor_queries(arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = arr[:]
        for i in range(1, len(xor)):
            xor[i] = ~xor[i - 1] & xor[i] | xor[i - 1] & ~xor[i]
        xor.append(0)
        return [(~xor[u - 1] & xor[v] | xor[u - 1] & ~xor[v]) for u, v in queries]
