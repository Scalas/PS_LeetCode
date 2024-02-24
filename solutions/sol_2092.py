from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_all_people(
        n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        ts = defaultdict(set)
        tm = defaultdict(set)
        for u, v, t in meetings:
            ts[t].add((u, v))
            tm[t].add(u)
            tm[t].add(v)
        owner = [False] * n
        owner[0] = True
        owner[firstPerson] = True

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
            if x not in u:
                u[x] = -1
            if u[x] < 0:
                return x
            u[x] = find(u, u[x])
            return u[x]

        for t in sorted(ts.keys()):
            us = dict()
            ms = ts[t]
            mems = tm[t]
            for u, v in ms:
                union(us, u, v)
            notified_set = set()
            for m in mems:
                if owner[m]:
                    notified_set.add(find(us, m))
            for m in mems:
                if find(us, m) in notified_set:
                    owner[m] = True

        return [i for i in range(n) if owner[i]]
