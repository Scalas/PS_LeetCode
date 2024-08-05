from typing import List


class Solution:
    @staticmethod
    def range_sum(nums: List[int], n: int, left: int, right: int) -> int:
        for i in range(1, n):
            nums[i] += nums[i - 1]
        nums.append(0)

        count = [0] * 100001
        total = 0
        for i in range(n):
            for j in range(i, n):
                count[nums[j] - nums[i - 1]] += 1
                total += 1

        l, r = left - 1, total - right
        for i in range(100001):
            if count[i] >= l:
                count[i] -= l
                break
            else:
                l -= count[i]
                count[i] = 0

        for i in range(100000, -1, -1):
            if count[i] >= r:
                count[i] -= r
                break
            else:
                r -= count[i]
                count[i] = 0

        answer = 0
        mod = 10**9 + 7
        for i in range(100001):
            if count[i] == 0:
                continue
            answer = (answer + count[i] * i) % mod

        return answer
