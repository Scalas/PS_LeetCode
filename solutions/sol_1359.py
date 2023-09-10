class Solution:
    @staticmethod
    def count_orders(n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 1
        slot = 3
        res = 1
        for i in range(2, n + 1):
            res = (res * (slot * (slot + 1) // 2)) % mod
            slot += 2
        return res
