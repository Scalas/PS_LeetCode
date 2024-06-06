from typing import List


class Solution:
    @staticmethod
    def common_chars(words: List[str]) -> List[str]:
        min_count = [100] * 26
        for word in words:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            for i in range(26):
                min_count[i] = min(min_count[i], count[i])
        res = []
        for i in range(26):
            c = chr(i + ord("a"))
            res.extend([c] * min_count[i])
        return res
