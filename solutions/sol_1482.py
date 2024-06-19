from typing import List


class Solution:
    @staticmethod
    def min_days(bloom_day: List[int], m: int, k: int) -> int:
        n = len(bloom_day)
        if m * k > n:
            return -1

        def check(days):
            cnt = 0
            pre = 0
            for d in bloom_day:
                if d > days:
                    pre = 0
                    continue
                if pre == k - 1:
                    cnt += 1
                    pre = 0
                else:
                    pre += 1
            return cnt >= m

        s, e = 1, 10**9
        while s < e:
            mid = (s + e) // 2
            if check(mid):
                e = mid
            else:
                s = mid + 1
        return e
