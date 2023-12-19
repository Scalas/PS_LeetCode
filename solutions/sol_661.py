from math import floor
from typing import List


class Solution:
    @staticmethod
    def image_smoother(img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        answer = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                s = img[i][j]
                t = 1
                if i > 0:
                    if j > 0:
                        s += img[i - 1][j - 1]
                        t += 1
                    if j < m - 1:
                        s += img[i - 1][j + 1]
                        t += 1
                    s += img[i - 1][j]
                    t += 1
                if j > 0:
                    s += img[i][j - 1]
                    t += 1
                if j < m - 1:
                    s += img[i][j + 1]
                    t += 1
                if i < n - 1:
                    if j > 0:
                        s += img[i + 1][j - 1]
                        t += 1
                    if j < m - 1:
                        s += img[i + 1][j + 1]
                        t += 1
                    s += img[i + 1][j]
                    t += 1
                answer[i][j] = floor(s / t)
        return answer
