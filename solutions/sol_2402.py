from heapq import heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def most_booked(n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        q = list(range(n))
        nq = []
        count = [0] * n
        for u, v in meetings:
            while nq and nq[0][0] <= u:
                end, room = heappop(nq)
                heappush(q, room)
            if q:
                room = heappop(q)
                heappush(nq, (v, room))
                count[room] += 1
            else:
                end, room = heappop(nq)
                heappush(nq, (end + v - u, room))
                count[room] += 1

        mc = max(count)
        for i in range(n):
            if count[i] == mc:
                return i
        return -1
