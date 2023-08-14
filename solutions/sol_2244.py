from collections import defaultdict
from typing import List

INF = 10**9


class Solution:
    @staticmethod
    def minimum_rounds(tasks: List[int]) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        count = count.values()
        dp = [0] * (max(3, max(count)) + 1)
        dp[1] = -1
        dp[2] = dp[3] = 1
        for i in range(2, len(dp)):
            res = INF
            if dp[i - 2] >= 0:
                res = min(res, dp[i - 2] + 1)
            if dp[i - 3] >= 0:
                res = min(res, dp[i - 3] + 1)
            dp[i] = -1 if res == INF else res

        answer = 0
        for c in count:
            if dp[c] == -1:
                return -1
            answer += dp[c]
        return answer
