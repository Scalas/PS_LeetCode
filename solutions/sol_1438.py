from heapq import heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def longest_subarray(nums: List[int], limit: int) -> int:
        n = len(nums)
        answer = 0
        min_buf, max_buf = [], []
        deleted = -1
        for i in range(n):
            heappush(min_buf, (nums[i], i))
            heappush(max_buf, (-nums[i], i))
            while -min_buf[0][0] - max_buf[0][0] > limit:
                deleted += 1
                while min_buf and min_buf[0][1] <= deleted:
                    heappop(min_buf)
                while max_buf and max_buf[0][1] <= deleted:
                    heappop(max_buf)
            answer = max(answer, i - deleted)
        answer = max(answer, n - 1 - deleted)
        return answer
