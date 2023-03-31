from typing import List


class Solution:
    @staticmethod
    def ways(pizza: List[str], k: int) -> int:
        mod = 10 ** 9 + 7
        n, m = len(pizza), len(pizza[0])
        if n + m - 1 < k:
            return 0

        h_acc = [[0] * (m + 1) for _ in range(n)]
        v_acc = [[0] * m for _ in range(n + 1)]
        total = 0
        for i in range(n):
            for j in range(m):
                a = 1 if pizza[i][j] == 'A' else 0
                h_acc[i][j] = a
                if j > 0:
                    h_acc[i][j] += h_acc[i][j - 1]
                v_acc[i][j] = a
                if i > 0:
                    v_acc[i][j] += v_acc[i - 1][j]
                total += a

        # dp[i][j][k] 는 남은 피자가 i행 j열부터 n - 1 행 m - 1 열 까지이고
        # 잘라야할 횟수가 k 번일 때, 가능한 모든 경우의 수
        dp = [[[-1] * k for _ in range(m)] for _ in range(n)]

        def dfs(r, c, count, remain):
            if count == 0:
                return 1 if remain else 0

            if r == n or c == m:
                return 0

            if dp[r][c][count] == -1:
                res = 0
                # 수평으로 자르기
                apple = 0
                for i in range(r, n - 1):
                    apple += h_acc[i][m - 1] - h_acc[i][c - 1]
                    if apple:
                        res += dfs(i + 1, c, count - 1, remain - apple)
                apple = 0
                for i in range(c, m - 1):
                    apple += v_acc[n - 1][i] - v_acc[r - 1][i]
                    if apple:
                        res += dfs(r, i + 1, count - 1, remain - apple)
                dp[r][c][count] = res
            return dp[r][c][count]

        return dfs(0, 0, k - 1, total) % mod
