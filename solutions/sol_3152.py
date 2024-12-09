from typing import List


class Solution:
    @staticmethod
    def is_array_special(nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        acc = [0] * n
        for i in range(1, n):
            iv = 1 if nums[i] % 2 == nums[i - 1] % 2 else 0
            acc[i] = acc[i - 1] + iv
        return [acc[e] - acc[s] == 0 for s, e in queries]
