class Solution:
    @staticmethod
    def can_make_subsequence(str1: str, str2: str) -> bool:
        n, cur = len(str2), 0
        for c in str1:
            nxt_c = "a" if c == "z" else chr(ord(c) + 1)
            if str2[cur] in [c, nxt_c]:
                cur += 1
                if cur == n:
                    return True
        return False
