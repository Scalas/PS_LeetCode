from typing import List


class Solution:
    @staticmethod
    def max_width_of_vertical_area(points: List[List[int]]) -> int:
        xs = set()
        for u, v in points:
            xs.add(u)

        pre, *xs = sorted(xs)
        answer = 0
        for x in xs:
            answer = max(answer, x - pre)
            pre = x
        return answer
