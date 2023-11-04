from typing import List


class Solution:
    @staticmethod
    def get_last_moment(n: int, left: List[int], right: List[int]) -> int:
        l = n - min(right) if right else 0
        r = max(left) if left else 0
        return max(l, r)
