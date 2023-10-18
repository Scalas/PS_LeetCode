from typing import List


class Solution:
    @staticmethod
    def minimum_time(n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n)]
        degree = [0] * n
        for i in range(len(relations)):
            u, v = relations[i]
            g[u - 1].append(v - 1)
            degree[v - 1] += 1

        q = [i for i in range(n) if degree[i] == 0]
        pre_time = [0] * n
        answer = 0
        while q:
            nq = []
            for cur in q:
                cost = time[cur] + pre_time[cur]
                answer = max(answer, cost)
                for nxt in g[cur]:
                    degree[nxt] -= 1
                    pre_time[nxt] = max(pre_time[nxt], cost)
                    if not degree[nxt]:
                        nq.append(nxt)
            q = nq
        return answer
