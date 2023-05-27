from typing import List
INF = 10 ** 9


class Solution:
    @staticmethod
    def stone_game_3(stone_value: List[int]) -> str:
        n = len(stone_value)
        total = sum(stone_value)
        for i in range(1, n):
            stone_value[i] += stone_value[i - 1]
        stone_value.append(0)

        def dfs(cur, turn):
            if cur == n:
                return 0
            if dp[cur][turn] == -INF:
                if turn:
                    res = INF
                    for i in range(3):
                        nxt = cur + i + 1
                        if nxt > n:
                            continue
                        res = min(res, dfs(nxt, 1 - turn))
                else:
                    res = -INF
                    for i in range(3):
                        nxt = cur + i + 1
                        if nxt > n:
                            continue
                        res = max(res, dfs(nxt, 1 - turn) + stone_value[nxt - 1] - stone_value[cur - 1])
                dp[cur][turn] = res
            return dp[cur][turn]

        dp = [[-INF] * 2 for _ in range(n)]
        dfs(0, 0)
        diff = dp[0][0] * 2 - total
        return 'Alice' if diff > 0 else ('Bob' if diff < 0 else 'Tie')
