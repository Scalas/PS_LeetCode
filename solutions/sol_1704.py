class Solution:
    @staticmethod
    def halves_are_alike(s: str) -> bool:
        h = len(s) // 2
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        return sum(map(lambda x: 1 if x in vowel else 0, s[:h])) == sum(
            map(lambda x: 1 if x in vowel else 0, s[h:])
        )
