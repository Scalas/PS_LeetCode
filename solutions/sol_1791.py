from typing import List


class Solution:
    @staticmethod
    def find_center(edges: List[List[int]]) -> int:
        s = set()
        for u, v in edges:
            if u in s:
                return u
            s.add(u)
            if v in s:
                return v
            s.add(v)
