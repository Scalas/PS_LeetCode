from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        begin = defaultdict(int)
        end = defaultdict(int)
        pos = set()
        for u, v in intervals:
            begin[u] += 1
            end[v] += 1
            pos.add(u)
            pos.add(v)

        u, v = new_interval
        begin[u] += 1
        end[v] += 1
        pos.add(u)
        pos.add(v)

        pos = sorted(pos)
        s, e, pre = 0, 0, 0
        count = 0
        answer = []
        for x in pos:
            count += begin[x]
            if count:
                if not pre:
                    s = x
                    pre = count
            count -= end[x]
            if not count:
                if pre:
                    answer.append([s, x])
            pre = count
        return answer
