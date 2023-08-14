class Solution:
    @staticmethod
    def check_inclusion(s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        a_ord = ord("a")
        for i in range(n):
            s1_count[ord(s1[i]) - a_ord] += 1
            s2_count[ord(s2[i]) - a_ord] += 1
        if s1_count == s2_count:
            return True
        for i in range(m - n):
            s2_count[ord(s2[n + i]) - a_ord] += 1
            s2_count[ord(s2[i]) - a_ord] -= 1
            if s1_count == s2_count:
                return True
        return False
