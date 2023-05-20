from typing import List


class Solution:
    @staticmethod
    def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n, m = len(equations), len(queries)
        index = dict()
        idx = 0
        g = []
        for i in range(n):
            o1, o2 = equations[i]
            res = values[i]
            if o1 not in index:
                index[o1] = idx
                idx += 1
            if o2 not in index:
                index[o2] = idx
                idx += 1
            while len(g) < idx:
                g.append([])
            i1, i2 = index[o1], index[o2]
            g[i1].append([i2, res])
            g[i2].append([i1, 1 / res])

        def calc(x, y):
            q = [(x, 1)]
            visited = [False] * len(g)
            visited[x] = True
            while q:
                nq = []
                for cur, rate in q:
                    for nxt, nrate in g[cur]:
                        if nxt == y:
                            return rate * nrate
                        if visited[nxt]:
                            continue
                        visited[nxt] = True
                        nq.append((nxt, rate * nrate))
                q = nq
            return -1.0

        answer = []
        for o1, o2 in queries:
            if o1 not in index or o2 not in index:
                answer.append(-1.0)
                continue
            i1, i2 = index[o1], index[o2]
            answer.append(calc(i1, i2))
        return answer
