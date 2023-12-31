class Solution:
    @staticmethod
    def max_length_between_equal_characters(s: str) -> int:
        answer = -1
        for c in "abcdefghijklmnopqrstuvwxyz":
            if s.count(c) < 2:
                continue
            answer = max(answer, s.rindex(c) - s.index(c) - 1)
        return answer
