from typing import List


class Solution:
    @staticmethod
    def count_consistent_strings(allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(
            [
                1 if len([c for c in word if c not in allowed]) == 0 else 0
                for word in words
            ]
        )
