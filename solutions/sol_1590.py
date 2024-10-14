from typing import List


class Solution:
    @staticmethod
    def min_subarray(nums: List[int], p: int) -> int:
        n = len(nums)
        r = sum(nums) % p
        if r == 0:
            return 0
        q = dict()
        acc = 0
        cand = []
        for i in range(n):
            acc = (acc + nums[i]) % p
            if acc == r:
                cand.append(i + 1)
            x1, x2 = acc + p - r, acc - r
            if x1 in q:
                cand.append(i - q[x1])
            if x2 in q:
                cand.append(i - q[x2])
            q[acc] = i
        res = min(cand) if cand else -1
        if res == n:
            return -1
        return res
