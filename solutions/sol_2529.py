from typing import List


class Solution:
    @staticmethod
    def maximum_count(nums: List[int]) -> int:
        n, p = 0, 0
        for num in nums:
            if num < 0:
                n += 1
            elif num > 0:
                p += 1
            else:
                pass
        return max(n, p)
