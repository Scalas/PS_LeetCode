from bisect import bisect_right
from typing import List


class Solution:
    @staticmethod
    def job_scheduling(
        startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(startTime)
        q = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        q.sort(key=lambda x: x[1])

        last = [0]
        max_p = [0]

        for s, e, p in q:
            res = max_p[-1]
            pre = bisect_right(last, s) - 1
            res = max(res, max_p[pre] + p)
            if last[-1] == e:
                max_p[-1] = max(max_p[-1], res)
            else:
                last.append(e)
                max_p.append(res)
        return max_p[-1]
