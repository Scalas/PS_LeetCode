from typing import List


class Solution:
    @staticmethod
    def remove_stones(stones: List[List[int]]) -> int:
        n, m = 0, 0
        for u, v in stones:
            n = max(n, u + 1)
            m = max(m, v + 1)
        row, col = [0] * n, [0] * m
        for u, v in stones:
            row[u] += 1
            col[v] += 1

        def remove_min():
            res = -1
            minx, miny = 10**9, 10**9
            for i in range(len(stones)):
                cu, cv = stones[i]
                if cu == cv == -1:
                    continue
                cminx, cminy = row[cu] - 1, col[cv] - 1
                if cminx > cminy:
                    cminx, cminy = cminy, cminx
                if cminx == 0 and cminy == 0:
                    continue
                if cminx < minx or (cminx == minx and cminy < miny):
                    res = i
                    minx, miny = cminx, cminy
            if res == -1:
                return False
            ru, rv = stones[res]
            row[ru] -= 1
            col[rv] -= 1
            stones[res] = [-1, -1]

            return True

        answer = 0
        while remove_min():
            answer += 1
        return answer
