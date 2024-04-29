from typing import List


class Solution:
    @staticmethod
    def min_operations(nums: List[int], k: int) -> int:
        def xor(x, y):
            return (x & ~y) | (~x & y)

        init_xor = nums[0]
        for num in nums[1:]:
            init_xor = xor(init_xor, num)

        res = 0
        u, v = init_xor, k
        while u > 0 or v > 0:
            if u % 2 != v % 2:
                res += 1
            u //= 2
            v //= 2
        return res
