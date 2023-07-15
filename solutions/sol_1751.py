from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
    @staticmethod
    def max_value(events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        event_map = defaultdict(list)
        for i in range(n):
            event_map[events[i][0]].append(i)
        event_start_points = sorted(event_map.keys())
        m = len(event_start_points)
        dp = [[[-1] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

        def dfs(cur, remain, include):
            if cur == n:
                return 0
            if dp[cur][remain][include] < 0:
                s, e, v = events[cur]
                if include:
                    nxt_key_idx = bisect_left(event_start_points, e + 1)
                    if nxt_key_idx < m:
                        nxt = event_map[event_start_points[nxt_key_idx]][0]
                        res = v + dfs(nxt, remain, 0)
                        if remain:
                            res = max(res, v + dfs(nxt, remain - 1, 1))
                        dp[cur][remain][include] = res
                    else:
                        dp[cur][remain][include] = v
                else:
                    res = dfs(cur + 1, remain, 0)
                    if remain:
                        res = max(res, dfs(cur + 1, remain - 1, 1))
                    dp[cur][remain][include] = res
            return dp[cur][remain][include]

        return max(dfs(0, k, 0), dfs(0, k - 1, 1))
