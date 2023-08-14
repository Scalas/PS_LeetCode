from collections import defaultdict


class Solution:
    @staticmethod
    def knight_probability(n: int, k: int, row: int, column: int) -> float:
        q = {(row, column): 1}
        directions = [
            (1, 2),
            (2, 1),
            (1, -2),
            (2, -1),
            (-1, 2),
            (-2, 1),
            (-1, -2),
            (-2, -1),
        ]
        total = 8**k
        while q and k:
            nq = defaultdict(int)
            for pos, count in q.items():
                r, c = pos
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    nq[(nr, nc)] += count
            q = nq
            k -= 1
        return sum(q.values()) / total
