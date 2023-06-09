from bisect import bisect_right
from typing import List


class Solution:
    @staticmethod
    def next_greatest_letter(letters: List[str], target: str) -> str:
        idx = bisect_right(letters, target)
        return letters[idx] if idx < len(letters) else letters[0]
