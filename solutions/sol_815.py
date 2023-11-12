from typing import List


class Solution:
    @staticmethod
    def num_buses_to_destination(
        routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        n = len(routes)
        routes = list(map(lambda x: set(x), routes))
        g = [[] for _ in range(n)]
        start, end = set(), set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                inter = routes[i] & routes[j]
                if inter:
                    g[i].append(j)
                    g[j].append(i)
        for i in range(n):
            if source in routes[i]:
                start.add(i)
            if target in routes[i]:
                end.add(i)

        q = start
        answer = 0
        visited = [False] * n
        for i in q:
            visited[i] = True
        while q:
            answer += 1
            nq = []
            for cur in q:
                if cur in end:
                    return answer
                for nxt in g[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq
        return -1
