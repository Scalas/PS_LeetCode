from typing import List


class Solution:
    @staticmethod
    def minimum_time(time: List[int], total_trips: int) -> int:
        def check(given_time):
            available_trips = 0
            for t in time:
                available_trips += (given_time // t)
            return available_trips >= total_trips

        s, e = 0, min(time) * total_trips
        while s < e:
            mid = (s + e) // 2
            if check(mid):
                e = mid
            else:
                s = mid + 1
        return e
