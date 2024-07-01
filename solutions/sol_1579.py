from typing import List


class Solution:
    @staticmethod
    def max_num_edges_to_remove(n: int, edges: List[List[int]]) -> int:
        u = [-1] * (n + 1)

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

        common, alice, bob = [], [], []
        for t, v, w in edges:
            if t == 1:
                alice.append([v, w])
            elif t == 2:
                bob.append([v, w])
            elif t == 3:
                common.append([v, w])
            else:
                continue

        answer = 0
        for v, w in common:
            if not union(u, v, w):
                answer += 1
        au = u[:]
        for v, w in alice:
            if not union(au, v, w):
                answer += 1
        bu = u[:]
        for v, w in bob:
            if not union(bu, v, w):
                answer += 1

        if len([g for g in au if g < 0]) > 2:
            return -1
        if len([g for g in bu if g < 0]) > 2:
            return -1
        return answer
