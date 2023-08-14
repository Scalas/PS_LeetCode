from typing import List


class Solution:
    @staticmethod
    def stone_game_2(piles: List[int]) -> int:
        n = len(piles)
        for i in range(1, n):
            piles[i] += piles[i - 1]
        piles.append(0)
        dp = [[[-1] * 2 for _ in range(100)] for _ in range(n)]

        def dfs(cur, m, turn):
            if cur == n:
                return 0
            if dp[cur][m][turn] == -1:
                res = 0
                if turn:
                    res = 10**9
                    for i in range(m * 2):
                        nxt = cur + i + 1
                        if nxt > n:
                            break
                        res = min(res, dfs(nxt, max(m, i + 1), 1 - turn))
                else:
                    for i in range(m * 2):
                        nxt = cur + i + 1
                        if nxt > n:
                            break
                        res = max(
                            res,
                            dfs(nxt, max(m, i + 1), 1 - turn)
                            + piles[nxt - 1]
                            - piles[cur - 1],
                        )
                dp[cur][m][turn] = res
            return dp[cur][m][turn]

        answer = dfs(0, 1, 0)
        return answer
