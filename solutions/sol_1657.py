from collections import defaultdict


class Solution:
    @staticmethod
    def close_strings(word1: str, word2: str) -> bool:
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        for c in word1:
            c1[c] += 1
        for c in word2:
            c2[c] += 1
        return sorted(c1.values()) == sorted(c2.values()) and set(word1) == set(word2)
