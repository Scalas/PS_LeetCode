from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def restore_array(adjacent_pairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        INF = 10**6

        for u, v in adjacent_pairs:
            g[u].append(v)
            g[v].append(u)

        cur = -1
        for key in g:
            if len(g[key]) == 1:
                cur = key
                break

        answer = []
        pre = -INF
        while cur != INF:
            answer.append(cur)
            nxt = INF
            for cand in g[cur]:
                if cand == pre:
                    continue
                nxt = cand
                break
            pre, cur = cur, nxt
        return answer
