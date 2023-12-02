from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def count_characters(words: List[str], chars: str) -> int:
        count = defaultdict(int)
        for c in chars:
            count[c] += 1
        answer = 0
        for word in words:
            wc = defaultdict(int)
            for c in word:
                wc[c] += 1
            check = True
            for c, cnt in wc.items():
                if count[c] < cnt:
                    check = False
                    break
            if check:
                answer += len(word)
        return answer
