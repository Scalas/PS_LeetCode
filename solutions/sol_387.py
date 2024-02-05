from collections import defaultdict


class Solution:
    @staticmethod
    def first_unique_char(s: str) -> int:
        g = defaultdict(list)
        for i in range(len(s)):
            g[s[i]].append(i)
        g = [x[0] for x in list(g.values()) if len(x) == 1]
        return min(g) if g else -1
