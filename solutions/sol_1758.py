class Solution:
    @staticmethod
    def min_operations(s: str) -> int:
        n = len(s)
        alt_0 = ["0" if i % 2 else "1" for i in range(n)]
        alt_1 = ["1" if i % 2 else "0" for i in range(n)]

        u, v = 0, 0
        for i in range(n):
            if s[i] != alt_0[i]:
                u += 1
            if s[i] != alt_1[i]:
                v += 1
        return min(u, v)
