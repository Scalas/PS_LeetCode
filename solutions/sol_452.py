from typing import List


class Solution:
    @staticmethod
    def find_min_arrow_shots(points: List[List[int]]) -> int:
        points.sort()
        pre = points[0][1]
        answer = 0
        for u, v in points[1:]:
            if u > pre:
                pre = v
                answer += 1
            else:
                pre = min(pre, v)

        return answer + 1
