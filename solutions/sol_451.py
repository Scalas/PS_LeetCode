from collections import defaultdict


class Solution:
    @staticmethod
    def frequency_sort(s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        return "".join(sorted(list(s), key=lambda x: (-count[x], x)))
