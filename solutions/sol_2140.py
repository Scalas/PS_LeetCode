from typing import List


class Solution:
    @staticmethod
    def most_points(questions: List[List[int]]) -> int:
        dp = []
        while questions:
            u, v = questions.pop()
            idx = len(dp)
            res = u + (0 if idx - v - 1 < 0 else dp[idx - v - 1])
            if dp:
                res = max(res, dp[-1])
            dp.append(res)
        return dp[-1]
