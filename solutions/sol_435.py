from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def erase_overlap_intervals(intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        start_group = defaultdict(list)
        for i in range(n):
            start_group[intervals[i][0]].append(i)
        start = sorted(start_group.keys())
        dp = [0] * len(intervals)
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            s, e = intervals[i]
            nxt_idx = bisect_left(start, e)
            if nxt_idx == len(start):
                dp[i] = max(dp[i + 1], 1)
            else:
                nxt = start_group[start[nxt_idx]][0]
                dp[i] = max(dp[i + 1], dp[nxt] + 1)
        return n - max(dp)
