from typing import List


class Solution:
    @staticmethod
    def make_equal(words: List[str]) -> bool:
        count = [0] * 26
        n = len(words)
        for c in map(lambda x: ord(x) - ord("a"), "".join(words)):
            count[c] += 1
        for cnt in count:
            if cnt == 0:
                continue
            if cnt % n:
                return False
        return True
