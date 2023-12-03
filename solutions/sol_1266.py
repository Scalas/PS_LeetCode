from typing import List


class Solution:
    @staticmethod
    def min_time_to_visit_all_points(points: List[List[int]]) -> int:
        x, y = points[0]
        answer = 0
        for u, v in points[1:]:
            w, h = abs(u - x), abs(v - y)
            diag = min(w, h)
            voh = max(w, h) - diag
            answer += diag + voh
            x, y = u, v
        return answer
