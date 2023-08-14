from typing import List


class Solution:
    @staticmethod
    def closest_meeting_node(edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d1 = [-1] * n
        d1[node1] = 0
        node = node1
        dst = 0
        while edges[node] != -1:
            dst += 1
            nxt = edges[node]
            if d1[nxt] == -1:
                d1[nxt] = dst
                node = nxt
            else:
                break
        d2 = [-1] * n
        d2[node2] = 0
        node = node2
        dst = 0
        while edges[node] != -1:
            dst += 1
            nxt = edges[node]
            if d2[nxt] == -1:
                d2[nxt] = dst
                node = nxt
            else:
                break

        answer = -1
        dmax = 10**9
        for i in range(n):
            if d1[i] == -1 or d2[i] == -1:
                continue
            dm = max(d1[i], d2[i])
            if dm < dmax:
                answer, dmax = i, dm
        return answer
