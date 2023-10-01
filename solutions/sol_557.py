class Solution:
    @staticmethod
    def reverse_words(s: str) -> str:
        return " ".join(map(lambda x: x[::-1], s.split(" ")))
