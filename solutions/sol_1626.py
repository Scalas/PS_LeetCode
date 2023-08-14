from typing import List


class Solution:
    @staticmethod
    def best_team_score(scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        scores = [
            scores[idx]
            for idx in sorted([i for i in range(n)], key=lambda x: (ages[x], scores[x]))
        ]
        dp = [0] * n
        for i in range(n):
            pre = 0
            for j in range(i):
                if scores[j] <= scores[i]:
                    pre = max(pre, dp[j])
            dp[i] = scores[i] + pre
        return max(dp)
