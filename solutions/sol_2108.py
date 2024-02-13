from typing import List


class Solution:
    @staticmethod
    def first_palindrome(words: List[str]) -> str:
        words.append("")
        return [w for w in words if w == w[::-1]][0]
