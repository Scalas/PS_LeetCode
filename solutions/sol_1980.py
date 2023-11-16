from typing import List


class Solution:
    @staticmethod
    def find_different_binary_string(nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)

        def itob(num):
            res = []
            while num:
                res.append(num % 2)
                num //= 2
            res += [0] * (n - len(res))
            return "".join(map(str, res[::-1]))

        for i in range(1 << n):
            s = itob(i)
            if s not in nums:
                return s
