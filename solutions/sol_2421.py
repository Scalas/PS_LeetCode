from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def number_of_good_paths(vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        val_nodes = defaultdict(list)
        for i in range(n):
            val_nodes[vals[i]].append(i)

        edges = [[max(vals[u], vals[v]), u, v] for u, v in edges]
        edges.sort(reverse=True)

        def union(u, a, b):
            a = find(u, a)
            b = find(u, b)
            if a != b:
                if u[a] < u[b]:
                    u[a] += u[b]
                    u[b] = a
                else:
                    u[b] += u[a]
                    u[a] = b

        def find(u, x):
            if u[x] < 0:
                return x
            u[x] = find(u, u[x])
            return u[x]

        u = [-1] * n
        answer = 0
        val_nodes = sorted(val_nodes.items())
        for val, nodes in val_nodes:
            if len(nodes) < 2:
                continue
            while edges and edges[-1][0] <= val:
                _, i, j = edges.pop()
                union(u, i, j)
            group = defaultdict(int)
            for node in nodes:
                group[find(u, node)] += 1
            for count in group.values():
                answer += (count * (count - 1)) // 2
        return answer + n

