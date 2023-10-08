from typing import List


class Solution:
    @staticmethod
    def max_dot_product(nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        INF = 10**9

        max_mult = -INF
        for i in range(n):
            for j in range(m):
                max_mult = max(max_mult, nums1[i] * nums2[j])
        if max_mult < 0:
            return max_mult

        dp = [[-INF] * m for _ in range(n)]

        def dfs(
            u,
            v,
        ):
            if u == n or v == m:
                return 0
            if dp[u][v] == -INF:
                dp[u][v] = max(
                    dfs(u + 1, v),
                    dfs(u, v + 1),
                    dfs(u + 1, v + 1) + nums1[u] * nums2[v],
                )
            return dp[u][v]

        return dfs(0, 0)
