from typing import List


class Solution:
    @staticmethod
    def count_bits(n: int) -> List[int]:
        def bc(num):
            res = 0
            while num:
                res += num % 2
                num //= 2
            return res

        return list(map(bc, range(n + 1)))
