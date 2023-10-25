class Solution:
    @staticmethod
    def kth_grammar(n: int, k: int) -> int:
        d = 0
        h = (1 << (n - 1)) // 2
        while n > 1:
            n -= 1
            if k > h:
                k -= h
                d = 1 - d
            h //= 2
        return d
