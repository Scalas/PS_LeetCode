from typing import List
from heapq import heappush, heappop


class Solution:
    @staticmethod
    def max_run_time(n: int, batteries: List[int]) -> int:
        m = len(batteries)
        batteries.sort(reverse=True)
        cand = batteries[:n]
        remain = batteries[n:]

        def check(time):
            plus = [(0, num) for num in remain]
            for num in cand:
                while num < time:
                    if not plus:
                        return False
                    start, count = heappop(plus)
                    if start > num:
                        return False
                    borrow = min(count, time - num)
                    start += borrow
                    count -= borrow
                    if count:
                        heappush(plus, (start, count))
                    num += borrow
            return True

        s, e = min(batteries), sum(batteries) // n
        answer = 0
        while s <= e:
            mid = (s + e) // 2
            if check(mid):
                answer = mid
                s = mid + 1
            else:
                e = mid - 1
        return answer
