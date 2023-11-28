class Solution:
    @staticmethod
    def knight_dialer(n: int) -> int:
        g = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
        ]
        mod = 10**9 + 7

        q = [1] * 10
        for _ in range(n - 1):
            nq = [0] * 10
            for cur in range(10):
                for nxt in g[cur]:
                    nq[nxt] = (nq[nxt] + q[cur]) % mod
            q = nq

        return sum(q) % mod
