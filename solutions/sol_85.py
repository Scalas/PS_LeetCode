from typing import List


class Solution:
    @staticmethod
    def maximal_rectangle(matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

        answer = 0
        for heights in dp:
            heights.append(0)
            hist = []
            for h in heights:
                cnt = 0
                while hist and hist[-1][0] > h:
                    last_h, last_cnt = hist.pop()
                    cnt += last_cnt
                    answer = max(answer, last_h * cnt)
                if hist and hist[-1][0] == h:
                    hist[-1][1] += cnt + 1
                else:
                    hist.append([h, cnt + 1])
        return answer
