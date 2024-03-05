class Solution:
    @staticmethod
    def minimum_length(s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            p = s[0]
            l, r = 0, len(s) - 1
            while l < r and s[l] == p:
                l += 1
            while r > l and s[r] == p:
                r -= 1
            if l == len(s) - 1:
                return 1 if len(s) == 1 else 0
            s = s[l : r + 1]
        return len(s)
