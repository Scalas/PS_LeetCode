from typing import List


class Solution:
    @staticmethod
    def max_frequency(nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        acc = nums[:]
        acc.append(0)
        for i in range(1, n):
            acc[i] += acc[i - 1]

        def min_count(x, y):
            return nums[y] * (y - x + 1) - (acc[y] - acc[x - 1])

        def check(f):
            for i in range(n - f + 1):
                if min_count(i, i + f - 1) <= k:
                    return True
            return False

        answer = 0
        s, e = 1, n
        while s <= e:
            mid = (s + e) // 2
            if check(mid):
                answer = mid
                s = mid + 1
            else:
                e = mid - 1

        return answer
