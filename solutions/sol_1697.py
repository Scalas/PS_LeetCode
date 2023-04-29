from typing import List


class Solution:
    @staticmethod
    def distance_limited_paths_exist(n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edge_list.sort(key=lambda x: -x[2])
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x: x[2])

        u = [-1] * n

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

        answer = [False] * len(queries)
        for src, dest, limit, idx in queries:
            while edge_list and edge_list[-1][2] < limit:
                s, e, _ = edge_list.pop()
                union(u, s, e)
            answer[idx] = find(u, src) == find(u, dest)
        return answer
