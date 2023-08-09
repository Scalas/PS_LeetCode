from typing import List


class Solution:
    @staticmethod
    def minimize_max(nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        n = len(nums)
        nums.sort()

        def check(max_diff):
            used = [False] * n
            count = 0
            for i in range(n - 1):
                if used[i]:
                    continue
                cur, nxt = nums[i], nums[i + 1]
                if nxt - cur <= max_diff:
                    used[i + 1] = True
                    count += 1
            return count >= p

        s, e = 0, nums[-1] - nums[0]
        while s < e:
            mid = (s + e) // 2
            if check(mid):
                e = mid
            else:
                s = mid + 1
        return e
