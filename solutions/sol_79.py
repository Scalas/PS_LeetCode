from typing import List


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        word = list(word)

        def search(r, c, w, visited):
            if not w:
                return True
            visited[r][c] = True
            nxt = w.pop()
            res = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if visited[nr][nc]:
                    continue
                if board[nr][nc] != nxt:
                    continue
                if search(nr, nc, w, visited):
                    res = True
                    break
            w.append(nxt)
            visited[r][c] = False
            return res

        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]:
                    continue
                visited = [[False] * m for _ in range(n)]
                if search(i, j, word[:0:-1], visited):
                    return True
        return False
