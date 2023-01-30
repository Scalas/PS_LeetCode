class Solution:
    @staticmethod
    def tribonacci(n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        f1, f2, f3 = 0, 1, 1
        for _ in range(n - 2):
            f1, f2, f3 = f2, f3, f1 + f2 + f3
        return f3
