from typing import List


class Solution:
    @staticmethod
    def num_similar_groups(strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        u = [-1] * n

        def union(u, a, b):
            a = find(u, a)
            b = find(u, b)
            if a == b:
                return
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

        for i in range(n):
            sa = strs[i]
            for j in range(i):
                sb = strs[j]
                diff = 0
                for k in range(m):
                    if sa[k] != sb[k]:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2:
                    union(u, i, j)

        answer = 0
        for i in range(n):
            if u[i] < 0:
                answer += 1
        return answer
