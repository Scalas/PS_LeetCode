from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def max_uncrossed_lines(nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        index1 = defaultdict(list)
        index2 = defaultdict(list)
        for i in range(n):
            index1[nums1[i]].append(i)
        for i in range(m):
            index2[nums2[i]].append(i)

        dp = [[-1] * m for _ in range(n)]

        def dfs(cur, start):
            if cur >= n or start >= m:
                return 0
            if dp[cur][start] < 0:
                num = nums1[cur]
                index = index2[num]
                res = dfs(cur + 1, start)
                if index:
                    target = bisect_left(index, start)
                    if target < len(index):
                        res = max(res, dfs(cur + 1, index[target] + 1) + 1)
                dp[cur][start] = res
            return dp[cur][start]

        return dfs(0, 0)
