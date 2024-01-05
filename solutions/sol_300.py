from typing import List
from bisect import bisect_left


class Solution:
    @staticmethod
    def length_of_lis(nums: List[int]) -> int:
        q = []
        for num in nums:
            if not q or q[-1] < num:
                q.append(num)
            else:
                q[bisect_left(q, num)] = num
        return len(q)
