from typing import List


class Solution:
    @staticmethod
    def num_magic_squares_inside(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def check(sr, sc):
            s = [0] * 8
            rcd, rcs = sr - sc, sr + sc + 2
            ns = set()
            for i in range(sr, sr + 3):
                for j in range(sc, sc + 3):
                    num = grid[i][j]
                    if num < 1 or num > 9:
                        return 0
                    s[i - sr] += num
                    s[j - sc + 3] += num
                    if i - j == rcd:
                        s[6] += num
                    if j + i == rcs:
                        s[7] += num
                    ns.add(num)
            if len(set(s)) == 1 and len(ns) == 9:
                return 1
            return 0

        answer = 0
        for i in range(n - 2):
            for j in range(m - 2):
                answer += check(i, j)
        return answer
