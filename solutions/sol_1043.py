from typing import List


class Solution:
    @staticmethod
    def max_sum_after_partitioning(arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def dfs(cur):
            if cur == n:
                return 0
            if dp[cur] == -1:
                res = 0
                maxv = 0
                for end in range(cur, min(n, cur + k)):
                    maxv = max(maxv, arr[end])
                    res = max(res, dfs(end + 1) + maxv * (end - cur + 1))
                dp[cur] = res
            return dp[cur]

        return dfs(0)
