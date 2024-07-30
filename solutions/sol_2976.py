from typing import List


class Solution:
    @staticmethod
    def minimum_cost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = float("inf")
        n = 26
        adj = [[inf] * n for _ in range(n)]

        def atoi(s):
            return list(map(lambda x: ord(x) - ord("a"), s))

        original = atoi(original)
        changed = atoi(changed)
        for i in range(n):
            adj[i][i] = 0
        for i in range(len(original)):
            u, v, w = original[i], changed[i], cost[i]
            if u == v:
                continue
            adj[u][v] = min(adj[u][v], w)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        source = atoi(source)
        target = atoi(target)
        answer = 0
        for i in range(len(source)):
            src, dst = source[i], target[i]
            answer += adj[src][dst]
        return answer if answer != inf else -1
