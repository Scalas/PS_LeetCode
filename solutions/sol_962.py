from typing import List


class Solution:
    @staticmethod
    def max_width_ramp(nums: List[int]) -> int:
        index = {nums[0]: 0}
        q = [nums[0]]

        def resolve_start(x, xi):
            s, e = 0, len(q) - 1
            res = xi
            while s <= e:
                mid = (s + e) // 2
                if q[mid] <= x:
                    res = index[q[mid]]
                    e = mid - 1
                else:
                    s = mid + 1
            return res

        answer = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num < q[-1]:
                q.append(num)
                index[num] = i
            else:
                answer = max(answer, i - resolve_start(num, i))
        return answer
