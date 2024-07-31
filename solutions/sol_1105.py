from typing import List


class Solution:
    @staticmethod
    def min_height_shelves(books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [[-1] * n for _ in range(n)]

        def dfs(shelf, start):
            if start == n:
                return 0
            if dp[shelf][start] == -1:
                w, h = 0, 0
                res = float("inf")
                for i in range(start, n):
                    cw, ch = books[i]
                    if w + cw > shelf_width:
                        break
                    w += cw
                    h = max(h, ch)
                    res = min(res, h + dfs(shelf + 1, i + 1))
                dp[shelf][start] = res
            return dp[shelf][start]

        return dfs(0, 0)
