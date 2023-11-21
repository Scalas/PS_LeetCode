from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def count_nice_pairs(nums: List[int]) -> int:
        def rev(x):
            digit = []
            while x:
                digit.append(x % 10)
                x //= 10

            res = 0
            unit = 10 ** (len(digit) - 1)
            for d in digit:
                res += d * unit
                unit //= 10
            return res

        nums = list(map(lambda x: x - rev(x), nums))
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        answer = 0
        mod = 10**9 + 7
        for cnt in count.values():
            answer = (answer + (cnt * (cnt - 1) // 2)) % mod
        return answer
