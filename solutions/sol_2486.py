class Solution:
    @staticmethod
    def append_characters(s: str, t: str) -> int:
        m = len(t)
        target = 0
        for c in s:
            if target == m:
                return 0
            if c == t[target]:
                target += 1
        return m - target
