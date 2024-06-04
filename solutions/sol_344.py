from typing import List


class Solution:
    @staticmethod
    def reverse_string(s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
