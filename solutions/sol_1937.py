from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def max_points(points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp = [[-1] * m for _ in range(n)]
        left, right = [], []

        for i in range(m):
            dp[n - 1][i] = points[n - 1][i]
            heappush(right, [-(dp[n - 1][i] - i), i])
        for i in range(n - 2, -1, -1):
            next_right = []
            moved = [False] * m
            pre_dp = dp[i + 1]
            for j in range(m):
                cur = points[i][j]
                heappush(left, [-(pre_dp[j] + j), j])
                moved[j] = True
                while right and moved[right[0][1]]:
                    heappop(right)
                left_max = -left[0][0] - j
                right_max = -right[0][0] + j if right else 0
                dp[i][j] = cur + max(left_max, right_max)
                heappush(next_right, [-(dp[i][j] - j), j])
            left, right = [], next_right

        return max(dp[0])
