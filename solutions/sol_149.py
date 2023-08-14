import math
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def max_points(points: List[List[int]]) -> int:
        n = len(points)
        lines = set()
        answer = 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                px1, py1 = points[i]
                px2, py2 = points[j]
                if px1 == px2:
                    count = 2
                    for k in range(j + 1, n):
                        if points[k][0] == px1:
                            count += 1
                    answer = max(answer, count)
                    continue
                elif py1 == py2:
                    count = 2
                    for k in range(j + 1, n):
                        if points[k][1] == py1:
                            count += 1
                    answer = max(answer, count)
                    continue
                slope = (py1 - py2) / (px1 - px2)
                c = py1 - (slope * px1)
                line = (slope, c)
                if line in lines:
                    continue
                lines.add(line)
                count = 2
                for k in range(j + 1, n):
                    px, py = points[k]
                    if math.isclose(px * slope + c, py):
                        count += 1
                answer = max(answer, count)
        return answer

    @staticmethod
    def max_points_2(points: List[List[int]]) -> int:
        n = len(points)
        answer = 1
        for i in range(n - 1):
            x1, y1 = points[i]
            count = defaultdict(int)
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2:
                    count["inf"] += 1
                    continue
                count[(y1 - y2) / (x1 - x2)] += 1
            answer = max(answer, max(count.values()) + 1)
        return answer
