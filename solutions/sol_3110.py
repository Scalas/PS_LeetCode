class Solution:
    @staticmethod
    def score_of_string(s: str) -> int:
        return sum([abs(ord(s[i + 1]) - ord(s[i])) for i in range(len(s) - 1)])
