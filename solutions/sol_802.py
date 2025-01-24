from typing import List


class Solution:
    @staticmethod
    def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rg = [[] for _ in range(n)]
        degree = [0] * n
        for i in range(n):
            for j in graph[i]:
                rg[j].append(i)
                degree[i] += 1
        q = [i for i in range(n) if not graph[i]]

        answer = q[:]
        while q:
            nq = []
            for cur in q:
                for before in rg[cur]:
                    degree[before] -= 1
                    if degree[before] == 0:
                        nq.append(before)
                        answer.append(before)
            q = nq
        answer.sort()
        return answer
