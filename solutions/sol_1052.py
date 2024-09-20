from typing import List


class Solution:
    @staticmethod
    def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = sum([customers[i] * (1 - grumpy[i]) for i in range(n)])
        p = sum([customers[i] * grumpy[i] for i in range(minutes)])
        max_p = p
        for i in range(1, n - minutes + 1):
            if grumpy[i - 1] == 1:
                p -= customers[i - 1]
            if grumpy[i + minutes - 1] == 1:
                p += customers[i + minutes - 1]
            max_p = max(max_p, p)
        return base + max_p
