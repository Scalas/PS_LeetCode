from typing import List


class Solution:
    @staticmethod
    def dest_city(paths: List[List[str]]) -> str:
        start, end = set(), set()
        for u, v in paths:
            start.add(u)
            end.add(v)
        return list(end - start)[0]
