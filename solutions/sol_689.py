from typing import List


class Solution:
    @staticmethod
    def max_sum_of_three_sub_arrays(nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        nums.append(0)
        dp = [[-1] * 4 for _ in range(n)]
        trace = [[False] * 4 for _ in range(n)]

        def dfs(cur, count):
            nonlocal n, dp
            if cur > n - k or count == 0:
                return 0
            if dp[cur][count] == -1:
                skip = dfs(cur + 1, count)
                include = dfs(cur + k, count - 1) + nums[cur + k - 1] - nums[cur - 1]
                if skip > include:
                    dp[cur][count] = skip
                else:
                    dp[cur][count] = include
                    trace[cur][count] = True
            return dp[cur][count]

        dfs(0, 3)
        u, v = 0, 3
        res = []
        while v:
            if trace[u][v]:
                res.append(u)
                u += k
                v -= 1
            else:
                u += 1
        return res
