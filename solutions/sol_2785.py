class Solution:
    @staticmethod
    def sort_vowels(s: str) -> str:
        vs = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        v = [c for c in s if c in vs]
        v.sort(reverse=True)

        res = []
        for c in s:
            if c in vs:
                res.append(v.pop())
            else:
                res.append(c)
        return "".join(res)
