from typing import List


class Solution:
    @staticmethod
    def count_routes(locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10**9 + 7
        dp = [[-1] * (fuel + 1) for _ in range(n)]

        def dfs(cur, fuel):
            if dp[cur][fuel] == -1:
                res = 0
                if cur == finish:
                    res += 1
                for nxt in range(n):
                    if nxt == cur:
                        continue
                    diff = abs(locations[nxt] - locations[cur])
                    if diff <= fuel:
                        res = (res + dfs(nxt, fuel - diff)) % mod
                dp[cur][fuel] = res
            return dp[cur][fuel]

        return dfs(start, fuel)
