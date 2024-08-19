from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def nth_ugly_number(n: int) -> int:
        ugly: List[int] = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        if len(ugly) >= n:
            return ugly[n - 1]
        while len(ugly) < n:
            last = ugly[-1]
            num1 = ugly[bisect_left(ugly, (last + 2) // 2)] * 2
            num2 = ugly[bisect_left(ugly, (last + 3) // 3)] * 3
            num3 = ugly[bisect_left(ugly, (last + 5) // 5)] * 5
            num = min(num1, num2, num3)
            ugly.append(num)
        return ugly[-1]
