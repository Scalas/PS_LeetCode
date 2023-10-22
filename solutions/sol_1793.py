from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def maximum_score(nums: List[int], k: int) -> int:
        mins = set()
        left_min = []
        minv = nums[k]
        for i in range(k - 1, -1, -1):
            minv = min(minv, nums[i])
            left_min.append(minv)
            mins.add(minv)

        right_min = []
        minv = nums[k]
        for i in range(k + 1, len(nums)):
            minv = min(minv, nums[i])
            right_min.append(minv)
            mins.add(minv)

        left_min = left_min[::-1]
        right_min = right_min[::-1]

        answer = min(nums) * len(nums)
        for m in mins:
            left = bisect_left(left_min, m)
            right = bisect_left(right_min, m)
            length = len(left_min) + len(right_min) + 1 - left - right
            answer = max(answer, length * m)
        return answer
