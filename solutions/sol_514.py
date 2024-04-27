from collections import defaultdict


class Solution:
    @staticmethod
    def find_rotate_steps(ring: str, key: str) -> int:
        inf = float("inf")
        n = len(ring)
        m = len(key)
        pos = defaultdict(list)
        for i in range(n):
            pos[ring[i]].append(i)
        dp = [[-1] * m for _ in range(n)]

        def calc_move(i1, i2):
            if i1 < i2:
                i1, i2 = i2, i1
            d1 = i1 - i2
            d2 = (n - i1) + i2
            return min(d1, d2)

        def dfs(cur, target_idx):
            if target_idx == m:
                return 0
            if dp[cur][target_idx] == -1:
                res = inf
                target = key[target_idx]
                for nxt in pos[target]:
                    step = calc_move(cur, nxt) + 1
                    res = min(res, dfs(nxt, target_idx + 1) + step)
                dp[cur][target_idx] = res
            return dp[cur][target_idx]

        return dfs(0, 0)
