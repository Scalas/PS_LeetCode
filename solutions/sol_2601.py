from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def prime_sub_operation(nums: List[int]) -> bool:
        is_prime = [True] * 1001
        is_prime[0] = is_prime[1] = False
        for i in range(2, 501):
            for j in range(i * 2, 1001, i):
                is_prime[j] = False
        primes = [i for i in range(1001) if is_prime[i]]

        n = len(nums)
        m = len(primes)
        for i in range(n - 2, -1, -1):
            cur, nxt = nums[i], nums[i + 1]
            if cur >= nxt:
                diff = cur - nxt + 1
                sub_idx = bisect_left(primes, diff)
                if sub_idx == m:
                    return False
                sub = primes[sub_idx]
                if sub >= cur:
                    return False
                nums[i] -= sub
        return True
