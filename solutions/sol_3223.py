class Solution:
    @staticmethod
    def minimum_length(s: str) -> int:
        count = [0] * 26
        base = ord("a")
        for c in s:
            count[ord(c) - base] += 1
        answer = 0
        for c in count:
            if c == 0:
                continue
            answer += 1 if c % 2 else 2
        return answer
