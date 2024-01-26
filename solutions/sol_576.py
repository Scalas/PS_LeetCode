from collections import defaultdict


class Solution:
    @staticmethod
    def find_paths(
        m: int, n: int, max_move: int, start_row: int, start_column: int
    ) -> int:
        q = {(start_row, start_column): 1}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mod = 10**9 + 7
        answer = 0
        for _ in range(max_move):
            nq = defaultdict(int)
            for p, cnt in q.items():
                r, c = p
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        answer = (answer + cnt) % mod
                        continue
                    nq[(nr, nc)] += cnt
            q = nq
        return answer
