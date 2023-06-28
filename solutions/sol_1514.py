from heapq import heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def max_probability(n: int, edges: List[List[int]], succ_prob: List[float], start: int, end: int) -> float:
        g = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succ_prob[i]
            g[u].append((v, p))
            g[v].append((u, p))

        dp = [-1] * n
        dp[start] = 1
        q = [(-1, start)]
        while q:
            prob, cur = heappop(q)
            prob *= -1
            if prob < dp[cur]:
                continue
            for nxt, nxtProb in g[cur]:
                nprob = prob * nxtProb
                if dp[nxt] < nprob:
                    dp[nxt] = nprob
                    heappush(q, (-nprob, nxt))

        return dp[end] if dp[end] != -1 else 0
