class Solution:
    @staticmethod
    def pivot_integer(n: int) -> int:
        s = n * (n + 1) // 2
        sqrt = int(s**0.5)
        if sqrt**2 == s:
            return sqrt
        return -1
