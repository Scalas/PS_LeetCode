from typing import List


class Solution:
    @staticmethod
    def check_arithmetic_subarrays(
        nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        def check(x, y):
            line = sorted(nums[x : y + 1])
            if len(line) == 1:
                return True
            d = line[1] - line[0]
            for i in range(len(line) - 1):
                if line[i + 1] - line[i] != d:
                    return False
            return True

        return [check(u, v) for u, v in zip(l, r)]
