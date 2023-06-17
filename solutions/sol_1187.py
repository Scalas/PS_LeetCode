from bisect import bisect_right
from typing import List


class Solution:
    @staticmethod
    def make_array_increasing(arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n, m = len(arr1), len(arr2)

        dp = [dict() for _ in range(n)]

        def dfs(cur, last):
            if cur == n:
                return 0
            if dp[cur].get(last, -1) == -1:
                res = 2001
                num = arr1[cur]
                if num > last:
                    res = min(res, dfs(cur + 1, num))
                alt = bisect_right(arr2, last)
                if alt < m:
                    res = min(res, dfs(cur + 1, arr2[alt]) + 1)
                dp[cur][last] = res
            return dp[cur][last]

        answer = dfs(0, -1)
        return -1 if answer == 2001 else answer
