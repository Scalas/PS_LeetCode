from typing import List

INF = 10**9


class Solution:
    @staticmethod
    def min_taps(n: int, ranges: List[int]) -> int:
        tabs = []
        for i in range(n + 1):
            if ranges[i] == 0:
                continue
            tabs.append([max(i - ranges[i], 0), i + ranges[i]])
        tabs.sort()
        m = len(tabs)

        dp = [dict() for _ in range(m)]

        def dfs(cur, start):
            if start >= n:
                return 0
            if cur == m:
                return INF
            if tabs[cur][0] > start:
                return INF
            if dp[cur].get(start, -1) == -1:
                res = INF
                # include current tab
                res = min(res, dfs(cur + 1, tabs[cur][1]) + 1)

                # exclude current tab
                res = min(res, dfs(cur + 1, start))
                dp[cur][start] = res
            return dp[cur][start]

        answer = dfs(0, 0)
        return answer if answer != INF else -1
