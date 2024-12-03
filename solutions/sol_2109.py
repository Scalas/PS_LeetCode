from typing import List


class Solution:
    @staticmethod
    def add_spaces(s: str, spaces: List[int]) -> str:
        s = list(s)
        for i in spaces:
            s[i] = " " + s[i]
        return "".join(s)
