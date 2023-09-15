from typing import List


class Solution:
    @staticmethod
    def min_cost_connect_points(points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        edges = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                r1, c1 = points[i]
                r2, c2 = points[j]
                d = abs(r2 - r1) + abs(c2 - c1)
                edges.append((d, i, j))

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
            return False

        def find(u, x):
            if u[x] < 0:
                return x
            u[x] = find(u, u[x])
            return u[x]

        u = [-1] * n
        edges.sort()
        answer = 0
        count = 0
        for d, x, y in edges:
            res = union(u, x, y)
            if res:
                answer += d
                count += 1
                if count == n - 1:
                    return answer
        return -1
