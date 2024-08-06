from collections import defaultdict


class Solution:
    @staticmethod
    def minimum_pushes(word: str) -> int:
        count = defaultdict(int)
        for c in word:
            count[c] += 1
        rem = 8
        m = 1
        move = defaultdict(int)
        for c in sorted(set(word), key=lambda x: -count[x]):
            move[c] = m
            rem -= 1
            if rem == 0:
                m += 1
                rem = 8
        answer = 0
        for c, cnt in count.items():
            answer += cnt * move[c]
        return answer
