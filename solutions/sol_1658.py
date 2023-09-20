from typing import List


class Solution:
    @staticmethod
    def min_operations(nums: List[int], x: int) -> int:
        n = len(nums)
        INF = 10**9

        t = sum(nums) - x
        if t < 0:
            return -1
        if t == 0:
            return n
        s, e = 0, 0
        cur = 0
        answer = INF
        while True:
            while e < n and cur < t:
                cur += nums[e]
                e += 1
            if cur < t:
                break
            if cur == t:
                answer = min(answer, n + s - e)
            while cur >= t:
                cur -= nums[s]
                s += 1
                if cur == t:
                    answer = min(answer, n + s - e)
        return answer if answer != INF else -1
