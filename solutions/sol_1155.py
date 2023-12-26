from collections import defaultdict


class Solution:
    @staticmethod
    def num_rolls_to_target(n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        d = defaultdict(int)
        for i in range(1, k + 1):
            d[i] += 1
        for _ in range(n - 1):
            nd = defaultdict(int)
            for i in range(1, k + 1):
                for v, c in d.items():
                    nd[v + i] = (nd[v + i] + c) % mod
            d = nd
        return d.get(target, 0)
