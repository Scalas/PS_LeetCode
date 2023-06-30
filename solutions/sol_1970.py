from typing import List


class Solution:
    @staticmethod
    def latest_day_to_cross(row: int, col: int, cells: List[List[int]]) -> int:
        last = len(cells)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # cell (i, j) flooded on day (board[i][j])
        board = [[last + 1] * col for _ in range(row)]
        for i in range(len(cells)):
            r, c = cells[i]
            board[r - 1][c - 1] = i + 1

        def check(day):
            q = [(0, i) for i in range(col) if board[0][i] > day]
            visited = [[False] * col for _ in range(row)]
            while q:
                nq = []
                for cr, cc in q:
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if not (0 <= nr < row and 0 <= nc < col):
                            continue
                        if board[nr][nc] <= day:
                            continue
                        if visited[nr][nc]:
                            continue
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                q = nq
            res = False
            for i in range(col):
                if visited[row - 1][i]:
                    res = True
                    break
            return res

        s, e = 0, len(cells)
        answer = 0
        while s <= e:
            mid = (s + e) // 2
            if check(mid):
                answer = mid
                s = mid + 1
            else:
                e = mid - 1
        return answer
