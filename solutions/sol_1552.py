from typing import List


class Solution:
    @staticmethod
    def max_distance(position: List[int], m: int) -> int:
        s, e = 1, 10**9
        position.sort()

        def check(force):
            count = 0
            pre = -force
            for p in position:
                if p - force >= pre:
                    count += 1
                    pre = p
            return count >= m

        answer = 0
        while s <= e:
            mid = (s + e) // 2
            if check(mid):
                answer = max(answer, mid)
                s = mid + 1
            else:
                e = mid - 1
        return answer
