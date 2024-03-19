from collections import defaultdict
from heapq import heappop, heapify
from typing import List


class Solution:
    @staticmethod
    def least_interval(tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for key in tasks:
            count[key] += 1
        q = list(map(lambda x: -x, count.values()))
        heapify(q)
        answer = 0
        while q:
            nq = []
            count = 0
            for _ in range(n + 1):
                if q:
                    count += 1
                    nxt = heappop(q) + 1
                    if nxt != 0:
                        nq.append(nxt)
            q += nq
            if q:
                answer += n + 1
                heapify(q)
            else:
                answer += count
        return answer
