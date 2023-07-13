from typing import List


class Solution:
    @staticmethod
    def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(num_courses)]
        degree = [0] * num_courses
        for u, v in prerequisites:
            g[v].append(u)
            degree[u] += 1

        q = [i for i in range(num_courses) if not degree[i]]
        print(degree)
        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    degree[nxt] -= 1
                    if not degree[nxt]:
                        nq.append(nxt)
            q = nq
        return sum(degree) == 0
