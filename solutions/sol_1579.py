from typing import List


class Solution:
    @staticmethod
    def max_num_edges_to_remove(n: int, edges: List[List[int]]) -> int:
        au = [-1] * (n + 1)
        bu = [-1] * (n + 1)
        au[0] = bu[0] = 0

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
                return True
            else:
                return False

        def find(u, x):
            if u[x] < 0:
                return x
            u[x] = find(u, u[x])
            return u[x]

        connect = 0
        edges.sort(key=lambda x: -x[0])
        for t, o1, o2 in edges:
            connected = False
            if t % 2:
                connected = union(au, o1, o2)
            if t > 1:
                connected = union(bu, o1, o2)
            if connected:
                connect += 1

        if (
            sum(map(lambda x: 1 if x < 0 else 0, au)) > 1
            or sum(map(lambda x: 1 if x < 0 else 0, bu)) > 1
        ):
            return -1

        return len(edges) - connect
