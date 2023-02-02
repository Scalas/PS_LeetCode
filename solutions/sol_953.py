from typing import List


class Solution:
    @staticmethod
    def is_alien_sorted(words: List[str], order: str) -> bool:
        n = len(words)
        index = dict()
        for i in range(26):
            index[order[i]] = i
        for i in range(n):
            words[i] = list(map(lambda x: index[x], words[i]))
        for i in range(n - 1):
            if words[i] > words[i + 1]:
                return False
        return True
