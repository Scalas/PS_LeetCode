from heapq import heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def modified_graph_edges(
        n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        g = [dict() for _ in range(n)]
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w

        def dijkstra(src, dest, ignore_modifiable):
            nonlocal g
            inf = float("inf")
            dp = [inf] * n
            dp[src] = 0
            q = [[0, src]]
            pre = [-1] * n
            while q:
                dist, cur = heappop(q)
                if dist > dp[cur]:
                    continue
                for nxt, weight in g[cur].items():
                    if ignore_modifiable and weight == -1:
                        continue
                    new_dist = dist + abs(weight)
                    if new_dist < dp[nxt]:
                        dp[nxt] = new_dist
                        pre[nxt] = cur
                        heappush(q, [new_dist, nxt])
            return dp[dest], pre

        def modify(org_edges, trace_arr, shortest_dist):
            res = org_edges[:]
            cal = target - shortest_dist
            shortest_path = set()
            p = destination
            while p != -1:
                pre = trace_arr[p]
                shortest_path.add((pre, p))
                shortest_path.add((p, pre))
                p = pre

            modified = False
            for i in range(len(res)):
                cu, cv, cw = res[i]
                if cw != -1:
                    continue
                if (cu, cv) in shortest_path:
                    if not modified:
                        res[i] = [cu, cv, cal + 1]
                        modified = True
                else:
                    res[i] = [cu, cv, target + 1]
                g[cu][cv] = g[cv][cu] = res[i][2]

            return res

        if dijkstra(source, destination, True)[0] < target:
            return []

        shortest, trace = dijkstra(source, destination, False)
        answer = edges
        if shortest > target:
            return []
        while shortest < target:
            answer = modify(answer, trace, shortest)
            shortest, trace = dijkstra(source, destination, False)
        for i in range(len(answer)):
            if answer[i][2] == -1:
                answer[i][2] = 1
        return answer
