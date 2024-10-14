from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def smallest_chair(times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        fi = defaultdict(list)
        fo = defaultdict(list)
        ft = set()
        for i in range(n):
            u, v = times[i]
            fi[u].append(i)
            fo[v].append(i)
            ft.add(u)
            ft.add(v)
        seat = [-1] * n
        remain = [i for i in range(n)]
        for t in sorted(ft):
            for f in fo[t]:
                heappush(remain, seat[f])
            for f in fi[t]:
                seat[f] = heappop(remain)
        return seat[targetFriend]
