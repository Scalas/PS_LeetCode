from typing import List

INF = 10 ** 9


class Solution:
    @staticmethod
    def find_critical_and_pseudo_critical_edges(n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        edges = [edges[i] + [i] for i in range(m)]
        edges.sort(key=lambda x: x[2])

        def union(uni, a, b):
            a = find(uni, a)
            b = find(uni, b)
            if a != b:
                if uni[a] < uni[b]:
                    uni[a] += uni[b]
                    uni[b] = a
                else:
                    uni[b] += uni[a]
                    uni[a] = b
                return True
            return False

        def find(uni, x):
            if uni[x] < 0:
                return x
            uni[x] = find(uni, uni[x])
            return uni[x]

        def kruskal(extra=-1, include=False):
            uni = [-1] * n
            res = 0
            count = 0

            if include:
                eu, ev, ew, eidx = edges[extra]
                union(uni, eu, ev)
                res += ew
                count += 1

            for i in range(m):
                if i == extra:
                    continue
                u, v, w, idx = edges[i]
                if union(uni, u, v):
                    res += w
                    count += 1
                    if count == n - 1:
                        break
            if count != n - 1:
                return INF
            return res

        mst_cost = kruskal()
        answer = [[], []]

        for i in range(m):
            # exclude i
            ex_cost = kruskal(i, False)

            if ex_cost != mst_cost:
                answer[0].append(edges[i][3])
                continue

            # include i
            in_cost = kruskal(i, True)

            if in_cost == mst_cost:
                answer[1].append(edges[i][3])
        return answer
