from bisect import bisect_right
from typing import List


class Solution:
    @staticmethod
    def min_cost_tickets(days: List[int], costs: List[int]) -> int:
        n = len(days)
        last_day = days[-1]

        # cur 이전의 날 까지의 티케팅이 완료된 상태일 때
        # cur 포함 나머지 날을 모두 커버하기 위해 필요한 최소비용을 dp[cur] 이라고 한다
        dp = [-1] * (last_day + 1)

        def dfs(cur):
            if cur == n:
                return 0
            today = days[cur]
            if dp[today] == -1:
                res = dfs(bisect_right(days, today)) + costs[0]
                res = min(res, dfs(bisect_right(days, today + 6)) + costs[1])
                res = min(res, dfs(bisect_right(days, today + 29)) + costs[2])
                dp[today] = res
            return dp[today]

        return dfs(0)
