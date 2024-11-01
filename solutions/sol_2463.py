from typing import List


class Solution:
    @staticmethod
    def minimum_total_distance(robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        inf = 10**10

        n, m = len(factory), len(robot)

        def dfs(cur, ri):
            nonlocal n, m, dp
            if ri == m:
                return 0
            if cur == n:
                return (m - ri) * inf
            if dp[cur][ri] == -1:
                fp, count = factory[cur]
                res = dfs(cur + 1, ri)
                move = 0
                for i in range(ri, m):
                    if count == 0:
                        break
                    count -= 1
                    move += abs(robot[i] - fp)
                    res = min(res, dfs(cur + 1, i + 1) + move)
                dp[cur][ri] = res
            return dp[cur][ri]

        dp = [[-1] * m for _ in range(n)]
        return dfs(0, 0)
