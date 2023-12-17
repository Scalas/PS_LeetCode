class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        count = dict()
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1

        for c in count.values():
            if c:
                return False
        return True
