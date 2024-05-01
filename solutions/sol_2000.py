class Solution:
    @staticmethod
    def reverse_prefix(word: str, ch: str) -> str:
        idx = 0
        while idx < len(word) and word[idx] != ch:
            idx += 1
        if idx == len(word):
            return word
        return word[idx::-1] + word[idx + 1 :]
