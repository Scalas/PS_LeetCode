from typing import List


class Solution:
    @staticmethod
    def product_except_self(nums: List[int]) -> List[int]:
        p = 1
        zc = 0
        for num in nums:
            if num == 0:
                zc += 1
            else:
                p *= num
        if zc == 1:
            return list(map(lambda x: 0 if x else p, nums))
        if zc > 1:
            return [0] * len(nums)
        return list(map(lambda x: p // x, nums))
