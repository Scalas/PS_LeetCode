from typing import List


class Solution:
    @staticmethod
    def check_straight_line(coordinates: List[List[int]]) -> bool:
        xset = set([c[0] for c in coordinates])
        if len(xset) == 1:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        try:
            a = (y2 - y1) / (x2 - x1)
        except:
            return False
        b = y1 - a * x1
        for x, y in coordinates[2:]:
            if a * x + b != y:
                return False
        return True
