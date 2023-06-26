from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def total_cost(costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        q = []
        visited = [False] * n
        ls = set()
        for i in range(candidates):
            heappush(q, (costs[i], i))
            visited[i] = True
            ls.add(i)
        for i in range(n - 1, n - candidates - 1, -1):
            if not visited[i]:
                heappush(q, (costs[i], i))
                visited[i] = True
        li, ri = candidates - 1, n - candidates
        answer = 0
        c, idx = heappop(q)
        answer += c
        if idx in ls:
            li += 1
        else:
            ri -= 1
        for _ in range(k - 1):
            if li < n and not visited[li]:
                visited[li] = True
                heappush(q, (costs[li], li))
                ls.add(li)
            if ri >= 0 and not visited[ri]:
                visited[ri] = True
                heappush(q, (costs[ri], ri))
            c, idx = heappop(q)
            answer += c
            if idx in ls:
                li += 1
            else:
                ri -= 1
        return answer
