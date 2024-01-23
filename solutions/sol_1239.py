from typing import List


class Solution:
    @staticmethod
    def max_length(arr: List[str]) -> int:
        aid = dict()
        for c in range(26):
            aid[chr(c + ord("a"))] = 1 << c

        def dfs(cur, visit):
            if cur == len(arr):
                return 0

            if dp[cur].get(visit, -1) < 0:
                res = dfs(cur + 1, visit)
                possible = True
                for c in arr[cur]:
                    if aid[c] & visit:
                        possible = False
                        break
                if possible:
                    nvisit = visit
                    for c in arr[cur]:
                        nvisit |= aid[c]
                    res = max(res, dfs(cur + 1, nvisit) + len(arr[cur]))
                dp[cur][visit] = res
            return dp[cur][visit]

        arr = [s for s in arr if len(s) == len(set(s))]
        dp = [dict() for _ in range(len(arr))]
        return dfs(0, 0)
