from typing import List


class Solution:
    @staticmethod
    def ship_within_days(weights: List[int], days: int) -> int:
        def check(capacity):
            count = 0
            cargo = 0
            for w in weights:
                if cargo + w <= capacity:
                    cargo += w
                else:
                    cargo = w
                    count += 1
            if cargo:
                count += 1
            return count <= days

        s, e = max(weights), sum(weights)
        while s < e:
            mid = (s + e) // 2
            if check(mid):
                e = mid
            else:
                s = mid + 1
        return e
