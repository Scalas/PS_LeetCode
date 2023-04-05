from typing import List


class Solution:
    @staticmethod
    def minimize_array_value(nums: List[int]) -> int:
        n = len(nums)

        def check(m):
            cur = 0
            for i in range(n - 1, 0, -1):
                if nums[i] + cur > m:
                    cur = nums[i] + cur - m
                else:
                    cur = 0
            return cur + nums[0] <= m

        s, e = nums[0], max(nums)
        while s < e:
            mid = (s + e) // 2
            if check(mid):
                e = mid
            else:
                s = mid + 1
        return e
