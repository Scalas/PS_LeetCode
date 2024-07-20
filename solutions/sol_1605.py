from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def restore_matrix(row_sum: List[int], col_sum: List[int]) -> List[List[int]]:
        n, m = len(row_sum), len(col_sum)
        rq, cq = [], []
        for i in range(len(row_sum)):
            heappush(rq, [row_sum[i], 0, i])
        for i in range(len(col_sum)):
            heappush(cq, [col_sum[i], 1, i])

        mat = [[0] * m for _ in range(n)]
        inf = 10**9

        while rq and cq:
            num, t, idx = inf, -1, -1
            if rq:
                num, t, idx = rq[0]
            if cq:
                if cq[0][0] < num:
                    num, t, idx = cq[0]
            if t == 0:
                heappop(rq)
                cq[0][0] -= num
                mat[idx][cq[0][2]] = num
            else:
                heappop(cq)
                rq[0][0] -= num
                mat[rq[0][2]][idx] = num
        return mat
